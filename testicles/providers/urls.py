from django.urls import path

from .views import provider_view, provider_list_view, provider_detail_view, provider_request, ProviderDetail, ProviderRequestFormList, ProviderRequestDecison, ProviderDashboard


app_name = "providers"
urlpatterns = [
    path("", view=provider_list_view, name="list"),
    path("update/<int:pk>", view=provider_view, name="provider_view"),
    path("<int:pk>", view=ProviderDetail.as_view(), name="detail"),
    path("request", view=ProviderRequestFormList.as_view(), name="provider_request"),
    path("dashboard/<str:user_info>", view=ProviderDashboard.as_view(), name="test"),
    path("request/decision/<int:pk>", view=ProviderRequestDecison.as_view(), name="decision")
]