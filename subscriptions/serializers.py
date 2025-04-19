
from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for the Subscription model."""

    class Meta:
        model = Subscription
        fields = [
            'id',
            'name',
            'cost',
            'billing_cycle',
            'start_date',
            'renewal_date',
        ]
        read_only_fields = ['id', 'renewal_date']