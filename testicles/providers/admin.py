from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import ServiceProviders, Services, ProviderRequests

# Register your models here.



#admin.site.register(ServiceProviders)
@admin.register(ServiceProviders)
class ServiceProviderAdmin(admin.ModelAdmin):
     fields = ['user_info', 'about_me', 'short_description']
     list_display = ['name', 'date_joined']

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields = ('category', 'description', 'services', 'price', 'provider')
    list_display = ('category', 'services', 'price')

@admin.register(ProviderRequests)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('start_date',)
    fields = ['start_date', 'start_time', 'requested_service', 'requesting_user', 'provider',]

