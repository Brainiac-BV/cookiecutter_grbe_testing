from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth import get_user_model
from .models import ServiceProviders, Services, ProviderRequests, Categories
from .forms import ServiceProvidersAdminForm, ServiceChangeListForm

# Register your models here.



#admin.site.register(ServiceProviders)
@admin.register(ServiceProviders)
class ServiceProviderAdmin(admin.ModelAdmin):
     form = ServiceProvidersAdminForm
     
     list_display = ['name', 'date_joined', ]

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields = ('category', 'description', 'price', 'name')
    list_display = ('category', 'description', 'price', 'name')

@admin.register(ProviderRequests)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('start_date',)
    fields = ['start_date', 'start_time', 'requesting_user', 'provider',]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']

class ServiceChangeList(ChangeList):
    def __init__(self, request, model, list_display,
        list_display_links, list_filter, date_hierarchy,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin):
    
        super(ServiceChangeList, self).__init__(request, model,
            list_display, list_display_links, list_filter,
            date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable, 
            model_admin)
        
        # these need to be defined here, and not in MovieAdmin
        self.list_display = ['action_checkbox', 'name', 'category']
        self.list_display_links = ['category']
        self.list_editable = ['name']