from django.shortcuts import render
from django.views.generic import UpdateView, ListView, DetailView, CreateView
from django.forms import Select
from django.utils import timezone
from .models import ServiceProviders, Request

from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
# Create your views here.

'''
def provider_view(request):
    form = ServiceProviderForm()
    return render(request, 'providers/form.html', {'form':form} )   
'''

class ProviderView(UpdateView):
    model = ServiceProviders
    slug_field = "user_info_id"
    slug_url_kwarg = "user_info_id"


provider_view = ProviderView.as_view()

class ProviderListView(ListView):
    model = ServiceProviders
    #slug_field = "user_info"
    #slug_url_kwarg = "username"


provider_list_view = ProviderListView.as_view()

class ProviderDetailView(DetailView):
    model = ServiceProviders
    slug_field = "user_info_id"
    #slug_url_kwarg = "user_info_id"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = Request.objects.all()
        return context
provider_detail_view = ProviderDetailView.as_view()

class ProviderRequestCreateView(CreateView):
    model = Request
    fields = ['start_date', 'start_time', 'requested_service', 'sub_service',]
    def get_form(self):
         form = super().get_form()
         #sub_choices = Request.objects.get('sub_choices')
         form.fields['start_date'].widget = DatePickerInput()
         form.fields['start_time'].widget = TimePickerInput()
         form.fields['sub_service'].widget = Select() 
         return form 

provider_request = ProviderRequestCreateView.as_view()  