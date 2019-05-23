from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import ProviderRequests, Services
from .validators import date_valid


from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

class RequestForm(forms.ModelForm):
    
    class Meta:
        model = ProviderRequests
        fields = ["start_date", "start_time", "requested_service", "sub_service",] #("first_name, last_name, email, zip_code, services_chosen",)
        widgets = {
            "start_date": DatePickerInput(options={
                'minDate': str(date.today())
            }),
            "start_time": TimePickerInput(),        
       }

    def clean_start_date(self, *args, **kwargs):
           value =  self.cleaned_data.get('start_date')
           current_date = date.today()
           if value < current_date:
               raise ValidationError('in the past')
