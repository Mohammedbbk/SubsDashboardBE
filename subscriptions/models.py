from django.db import models
from django.utils import timezone


class Subscription(models.Model):
    MONTHLY = "monthly"
    ANNUALLY = "annually"
    BILLING_CYCLE_CHOICES = [
        (MONTHLY, "Monthly"),
        (ANNUALLY, "Annually"),
    ]

    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(max_length=10, choices=BILLING_CYCLE_CHOICES)
    start_date = models.DateField()
    renewal_date = models.DateField()
    annual_cost_option = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Optional: The cost if paid annually (for comparison)."
    )

    def __str__(self):
        return self.name


class PriceHistory(models.Model):
    subscription = models.ForeignKey(
        Subscription, related_name='price_history', on_delete=models.CASCADE
    )
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(
        max_length=10, choices=Subscription.BILLING_CYCLE_CHOICES
    )
    effective_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-effective_date']

    def __str__(self):
        return f"{self.subscription.name} - {self.cost} ({self.billing_cycle}) on {self.effective_date}"