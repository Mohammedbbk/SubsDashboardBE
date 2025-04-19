from django.urls import path
from . import views

urlpatterns = [
    path(
        "subscriptions/",
        views.SubscriptionListCreate.as_view(),
        name="subscription-list-create",
    ),
    path(
        "subscriptions/<int:pk>/",
        views.SubscriptionDestroy.as_view(),
        name="subscription-destroy",
    ),
]
