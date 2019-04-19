from django.shortcuts import render
from django.views.generic import UpdateView, ListView, DetailView, CreateView, FormView
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.forms import Select
from django.utils import timezone
from .models import ServiceProviders, Request
from .forms import RequestForm


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
    fields = ["about_me", "services_provided"]



provider_view = ProviderView.as_view()

class ProviderListView(ListView):
    model = ServiceProviders
    #slug_field = "user_info"
    #slug_url_kwarg = "username"


provider_list_view = ProviderListView.as_view()

class ProviderDetailView(DetailView):
    model = ServiceProviders
    slug_field = "user_info"
    slug_url_kwarg = "user_info"

    #slug_url_kwarg = "user_info_id"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RequestForm(initial={'provider': self.slug_url_kwarg})
        return context

provider_detail_view = ProviderDetailView.as_view()

class ProviderRequestFormView(SingleObjectMixin, FormView):
    form_class = RequestForm
    model = Request
    #fields = ['start_date', 'start_time', 'requested_service', 'sub_service',]
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

provider_request = ProviderRequestFormView.as_view()

class ProviderDetail(View):
    slug_field = "user_info"

    def get(self, request, *args, **kwargs):
        view = ProviderDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ProviderRequestFormView.as_view()
        return view(request, *args, **kwargs)