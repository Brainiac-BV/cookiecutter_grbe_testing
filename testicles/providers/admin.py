from django.contrib import admin

from .models import ServiceProvider, Services
# Register your models here.

admin.site.register(Services)
admin.site.register(ServiceProvider)