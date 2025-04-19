from django.urls import path
from . import views
from .views import DashboardSummaryView

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
    path(
        "dashboard-summary/",
        DashboardSummaryView.as_view(),
        name="dashboard-summary",
    ),
]
