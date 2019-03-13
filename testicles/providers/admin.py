from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import ServiceProviders
#from .forms import ServiceProviderForm

# Register your models here.



#admin.site.register(ServiceProviders)
@admin.register(ServiceProviders)
class ServiceProviderAdmin(admin.ModelAdmin):
     fields = ['services_chosen', 'user_info',]
 #   form = ServiceProviderForm

