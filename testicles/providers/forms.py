from django import forms
from .models import ProviderRequests


from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

class RequestForm(forms.ModelForm):
    class Meta:
        model = ProviderRequests
        fields = ["start_date", "start_time", "requested_service", "sub_service",] #("first_name, last_name, email, zip_code, services_chosen",)
        