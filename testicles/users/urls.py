from django.urls import path

from .views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
    user_delete_view,
    user_requests_made,
)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("dashboard/<str:username>/", view=user_detail_view, name="detail"),
    path("delete/<str:username>/", view=user_delete_view, name="delete"),
    path("requests/", view=user_requests_made, name="requests_made"),
]
