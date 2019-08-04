from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import ServiceProviders, Services, ProviderRequests, Categories
from .forms import ServiceProvidersAdminForm

# Register your models here.



#admin.site.register(ServiceProviders)
@admin.register(ServiceProviders)
class ServiceProviderAdmin(admin.ModelAdmin):
     form = ServiceProvidersAdminForm
     
     list_display = ['name', 'date_joined', ]

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields = ('category', 'description', 'serviceproviders', 'price',)
    list_display = ('category', 'serviceproviders', 'price')

@admin.register(ProviderRequests)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('start_date',)
    fields = ['start_date', 'start_time', 'requesting_user', 'provider',]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']