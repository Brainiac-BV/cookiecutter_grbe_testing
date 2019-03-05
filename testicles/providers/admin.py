from django.contrib import admin

from .models import ServiceProvider, ServiceProviderForm

# Register your models here.


#admin.site.register(ServiceProvider)
@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    form = ServiceProviderForm

