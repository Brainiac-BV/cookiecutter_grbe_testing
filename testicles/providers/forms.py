from django import forms
from django.core.exceptions import ValidationError

from datetime import date
from .models import ProviderRequests, Services, ServiceProviders


from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

class RequestForm(forms.ModelForm):
    class Meta:
        model = ProviderRequests
        fields = ["start_date", "start_time", "category", "services",]
        widgets = {
            "start_date": DatePickerInput(options={
                'minDate': str(date.today()),
            }),
            "start_time": TimePickerInput(), 
            "services": forms.widgets.CheckboxSelectMultiple()     
       }
    
    def __init__(self, prov, *args, **kwargs):
        prov = kwargs.pop('pk', None)
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['services'].queryset = Services.objects.filter(provider=prov)

class ServiceProvidersAdminForm(forms.ModelForm):
    class Meta:
        model = ServiceProviders
        fields = ['user_info', 'about_me', 'short_description', 'service_categories']
        widgets = {
            #'service_categories': forms.widgets.SelectMultiple( )
        }        