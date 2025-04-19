from django.shortcuts import render
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.db.models import Sum, Case, When, DecimalField, F
from rest_framework.views import APIView
from decimal import Decimal

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionListCreate(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Subscriptions.
    GET: Returns a list of all subscriptions.
    POST: Creates a new subscription.
    """

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        """
        Custom logic executed before saving a new subscription.
        Calculates the initial renewal_date.
        """
        start_date = serializer.validated_data.get("start_date", timezone.now().date())
        billing_cycle = serializer.validated_data.get("billing_cycle")

        renewal_date = None
        if billing_cycle == Subscription.MONTHLY:
            renewal_date = start_date + relativedelta(months=1)
        elif billing_cycle == Subscription.ANNUALLY:
            renewal_date = start_date + relativedelta(years=1)

        if renewal_date and renewal_date <= timezone.now().date():
            raise serializers.ValidationError(
                {
                    "renewal_date": f"Calculated renewal date ({renewal_date}) must be in the future."
                }
            )

        if renewal_date:
            serializer.save(renewal_date=renewal_date, start_date=start_date)
        else:
            raise serializers.ValidationError(
                {
                    "billing_cycle": "Could not calculate renewal date based on billing cycle."
                }
            )


class SubscriptionDestroy(generics.DestroyAPIView):
    """
    API endpoint for deleting a Subscription.
    DELETE: Deletes the subscription specified by ID in the URL.
    """

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class DashboardSummaryView(APIView):
    """
    Provides summary data for the dashboard, calculated via annotations.
    """
    def get(self, request, format=None):
        # Calculate total monthly spend using database aggregation
        monthly_cost_expression = Case(
            When(billing_cycle=Subscription.ANNUALLY, then=F('cost') / 12),
            When(billing_cycle=Subscription.MONTHLY, then=F('cost')),
            default=Decimal(0),  # Handle potential other cases or nulls
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )

        aggregation_result = Subscription.objects.aggregate(
            total_monthly_spend=Sum(
                monthly_cost_expression,
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        )

        total_monthly_spend = aggregation_result.get('total_monthly_spend') or Decimal(0)

        summary_data = {
            'total_monthly_spend': total_monthly_spend.quantize(Decimal("0.01")),
        }
        return Response(summary_data)
