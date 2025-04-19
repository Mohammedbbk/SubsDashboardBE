"""
URL configuration for mysite project.
... (rest of docstring) ...
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("subscriptions.urls")),
]