from django.urls import path
from . import views
from .views import DashboardSummaryView, SubscriptionUpdatePriceView, PriceHistoryListView

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
    path(
        "subscriptions/<int:pk>/update-price/",
        SubscriptionUpdatePriceView.as_view(),
        name="subscription-update-price",
    ),
    path(
        "subscriptions/<int:pk>/history/",
        PriceHistoryListView.as_view(),
        name="price-history-list",
    ),
]
