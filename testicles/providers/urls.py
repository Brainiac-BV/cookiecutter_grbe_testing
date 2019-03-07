from django.urls import path

from .views import provider_view, provider_list_view


app_name = "providers"
urlpatterns = [
    path("", view=provider_list_view, name="provider_list"),
    path("<str:username>/", provider_view, name="provider view"),
]