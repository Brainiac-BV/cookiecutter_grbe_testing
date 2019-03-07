'''
from django import forms
from .models import ServiceProviders
from django.views.generic import UpdateView

class ServiceProviderForm(UpdateView):
    #services_chosen = forms.MultipleChoiceField(choices=ServiceProvider.AVAILABLE_SERVICES)
    dates_available = forms.DateField()
    
    class Meta:
        model = ServiceProvider
        fields = "__all__" #("first_name, last_name, email, zip_code, services_chosen",)

'''