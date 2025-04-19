from django.db import models


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

    def __str__(self):
        return self.name
