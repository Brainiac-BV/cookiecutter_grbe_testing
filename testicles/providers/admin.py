from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import ServiceProviders, Services, Request
#from .forms import ServiceProviderForm

# Register your models here.



#admin.site.register(ServiceProviders)
@admin.register(ServiceProviders)
class ServiceProviderAdmin(admin.ModelAdmin):
     fields = ['services_provided', 'user_info', 'about_me']
     list_display = ['user_info',]

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'sub_choice')
    list_display = ('name',)

"""
@admin.register(SubServices)
class SubServicesAdmin(admin.ModelAdmin):
    fields = ['hair_choices', 'nail_choices', 'makeup_choices']
    list_display = ('hair_choices', 'nail_choices', 'makeup_choices',)

@admin.register(Appointments)
class AppointmentsAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)    
"""

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('start_date',)
    fields = ['start_date', 'start_time', 'requested_service', 'requesting_user', 'provider',]

