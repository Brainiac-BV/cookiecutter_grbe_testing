from django import forms
from django.forms import ModelMultipleChoiceField
from django.core.exceptions import ValidationError

from datetime import date
from .models import ProviderRequests, Services, ServiceProviders


from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
"""
class RequestServiceCHoiceField(ModelMultipleChoiceField):
    def queryset(self):
        provider = ServiceProviders.objects.filter(pk=)
"""
class ServiceProvidersForm(forms.ModelForm):
    class Meta:
        model = ServiceProviders
        fields = ["short_description", "about_me", "is_licensed", "service_categories", "zip_code", "services"]
        widgets = {
            "service_categories": forms.widgets.SelectMultiple()
        }


class RequestForm(forms.ModelForm):
    services = ModelMultipleChoiceField(queryset=Services.objects.all())
    
    def __init__(self, prov, *args, **kwargs):
        #prov = kwargs.pop('pk', None)
        #provider = ServiceProviders.objects.filter(pk=prov)
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['services'].queryset = Services.objects.filter(serviceproviders=prov).values_list('name', flat=True)
        print(prov)
        print([ServiceProviders.objects.filter(pk=prov)])
    
    class Meta:
        model = ProviderRequests
        fields = ["start_date", "start_time", "services",]
        widgets = {
            "start_date": DatePickerInput(options={
                'minDate': str(date.today()),
            }),
            "start_time": TimePickerInput(), 
            "services": forms.widgets.CheckboxSelectMultiple()     
       }
    
class ServiceProvidersAdminForm(forms.ModelForm):
    class Meta:
        model = ServiceProviders
        fields = ['user_info', 'about_me', 'short_description', 'service_categories', 'zip_code']
        widgets = {
            #'service_categories': forms.widgets.SelectMultiple( )
        }