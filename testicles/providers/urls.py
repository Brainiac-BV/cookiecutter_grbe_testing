from django.urls import path

from .views import provider_view


path("", provider_view, name="provider view")