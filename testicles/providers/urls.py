from django.urls import path

from .views import provider_view


app_name = "providers"
urlpatterns = [
    path("", provider_view, name="provider view"),
]