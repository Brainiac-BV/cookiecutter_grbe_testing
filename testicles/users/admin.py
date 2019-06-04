from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from testicles.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name", "zip_code", "service_provider_status", "profile_pic")}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name" ,"is_superuser"]
    search_fields = ["name", ]


