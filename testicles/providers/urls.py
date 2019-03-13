from django.urls import path

from .views import provider_view, provider_list_view, provider_detail_view


app_name = "providers"
urlpatterns = [
    path("", view=provider_list_view, name="list"),
    path("update/<int:pk>", view=provider_view, name="provider_view"),
    path("<int:pk>", view=provider_detail_view, name="detail"),
]