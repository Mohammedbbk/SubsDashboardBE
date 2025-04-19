from rest_framework import serializers
from decimal import Decimal
from .models import Subscription
from .models import PriceHistory


class SubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for the Subscription model."""

    monthly_cost = serializers.SerializerMethodField()
    annual_cost = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = [
            "id",
            "name",
            "cost",
            "billing_cycle",
            "start_date",
            "renewal_date",
            "monthly_cost",
            "annual_cost",
            "annual_cost_option",
        ]
        read_only_fields = ["id", "renewal_date", "monthly_cost", "annual_cost"]

    def get_monthly_cost(self, obj):
        """Calculates the equivalent monthly cost."""
        if obj.billing_cycle == Subscription.ANNUALLY:
            return (Decimal(obj.cost) / 12).quantize(Decimal("0.01"))
        elif obj.billing_cycle == Subscription.MONTHLY:
            return obj.cost
        return None

    def get_annual_cost(self, obj):
        """Calculates the equivalent annual cost."""
        if obj.billing_cycle == Subscription.MONTHLY:
            return (Decimal(obj.cost) * 12).quantize(Decimal("0.01"))
        elif obj.billing_cycle == Subscription.ANNUALLY:
            return obj.cost
        return None

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = ['id', 'subscription', 'cost', 'billing_cycle', 'effective_date']

class SubscriptionPriceUpdateSerializer(serializers.Serializer):
    cost = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    billing_cycle = serializers.ChoiceField(
        choices=Subscription.BILLING_CYCLE_CHOICES, required=False
    )
    # optional cycle change
