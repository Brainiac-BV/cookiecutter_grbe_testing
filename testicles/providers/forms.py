from django import forms
from .models import ProviderRequests
from .validators import date_valid


from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

class RequestForm(forms.ModelForm):
    start_date = forms.DateField(validators=[date_valid])
    
    class Meta:
        model = ProviderRequests
        fields = ["start_date", "start_time", "requested_service", "sub_service",] #("first_name, last_name, email, zip_code, services_chosen",)
        widgets = {
            'start_date': DatePickerInput()
        }