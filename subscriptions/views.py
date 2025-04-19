from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta
from django.utils import timezone

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
        start_date = serializer.validated_data.get('start_date', timezone.now().date())
        billing_cycle = serializer.validated_data.get('billing_cycle')

        renewal_date = None
        if billing_cycle == Subscription.MONTHLY:
            renewal_date = start_date + relativedelta(months=1)
        elif billing_cycle == Subscription.ANNUALLY:
            renewal_date = start_date + relativedelta(years=1)

        if renewal_date and renewal_date <= timezone.now().date():
            pass

        if renewal_date:
            serializer.save(renewal_date=renewal_date, start_date=start_date)
        else:
            super().perform_create(serializer)


class SubscriptionDestroy(generics.DestroyAPIView):
    """
    API endpoint for deleting a Subscription.
    DELETE: Deletes the subscription specified by ID in the URL.
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
