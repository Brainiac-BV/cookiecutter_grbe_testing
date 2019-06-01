from django.urls import path
from django_filters.views import FilterView

from .views import (provider_view, provider_list_view, provider_detail_view, provider_request, ProviderDetail, ProviderRequestFormList, ProviderRequestDecison, ProviderDashboard, ServiceCreationView,
ServiceListView, )
from .filters import ServicesFilter

app_name = "providers"
urlpatterns = [
    path("", view=provider_list_view, name="list"),
    path("update/<int:pk>", view=provider_view, name="provider_view"),
    path("<int:pk>", view=ProviderDetail.as_view(), name="detail"),
    path("request", view=ProviderRequestFormList.as_view(), name="provider_request"),
    path("dashboard/<str:user_info>", view=ProviderDashboard.as_view(), name="dash"),
    path("request/decision/<int:pk>", view=ProviderRequestDecison.as_view(), name="decision"),
    path("services/create", view=ServiceCreationView.as_view(), name="create_service"),
    path("services", view=ServiceListView.as_view(), name="service_list"),
    path("filter", view=FilterView.as_view(filterset_class=ServicesFilter,
        template_name='providers/serviceproviders_list.html'), name="filter")
]