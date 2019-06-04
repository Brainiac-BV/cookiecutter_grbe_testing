from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView, DetailView, CreateView, FormView, TemplateView
from django.views import View
from django.core.mail import send_mail
from allauth.account.models import EmailAddress

from postman.api import pm_write


from .models import ServiceProviders, ProviderRequests, Services
from .forms import RequestForm


# Create your views here.

class ProviderCreateView(LoginRequiredMixin,CreateView):
    model = ServiceProviders
    template_name = "providers/provider_signup.html"
    fields = ["short_description", "about_me", "is_licensed", "service_categories"]

class ProviderView(LoginRequiredMixin, UpdateView):
    model = ServiceProviders
    slug_field = "user_info_id"
    slug_url_kwarg = "user_info_id"
    fields = ["about_me", "service_categories"]



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

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['prov'] = self.kwargs.pop('pk')
        return kwargs 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RequestForm(prov=self.kwargs.pop('pk'))
        return context 
        
provider_detail_view = ProviderDetailView.as_view()

class ProviderRequestFormView(LoginRequiredMixin, CreateView):
    #form_class = RequestForm()
    model = ProviderRequests
    fields = ['start_date', 'start_time', 'category', 'services']

   

    def form_valid(self, form):
        form.instance.requesting_user_id = self.request.user
        form.instance.provider_id = self.kwargs.pop('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('providers:list')


provider_request = ProviderRequestFormView.as_view()

class ProviderDetail(View):
    #slug_field = "user_info"

    def get(self, request, *args, **kwargs):
        view = ProviderDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ProviderRequestFormView.as_view()
        return view(request, *args, **kwargs)


class ProviderRequestFormList(LoginRequiredMixin, ListView):
    model = ProviderRequests

    def get_queryset(self):
        """ Returns requests based on logged in provider_id"""
        provider = self.request.user.serviceproviders.pk
        return ProviderRequests.objects.filter(provider_id=provider).order_by('start_date')

class ProviderRequestDecison(LoginRequiredMixin, UpdateView):
    model = ProviderRequests
    fields = ['accepted', ]
    template_name = "providers/request_decision.html"
   
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.GET.get('username')
        #email2 = ProviderRequests.objects.get(requesting_user_id=user)
        if form.is_valid():
            if 'accept' in request.POST:
                pm_write(request.user, user,'test', 'test message',)
                return super().post(request, *args, **kwargs)
            elif 'deny' in request.POST:
                send_mail('test', 'test message 2', 'admin@grbe.co', [request.user.email])
                return super().post(request, *args, **kwargs)             

    def form_valid(self, form):
        if 'accept' in self.request.POST:
            form.instance.accepted = 'True'
        if 'deny' in self.request.POST:
            form.instance.accepted = 'False'
        return super(ProviderRequestDecison, self).form_valid(form)
    
class ProviderDashboard(LoginRequiredMixin, DetailView):
    model = ServiceProviders
    slug_field = "user_info"
    slug_url_kwarg = "user_info"
    template_name = "providers/serviceprovider_dash.html"
    
class ServiceCreationView(LoginRequiredMixin, CreateView):
    model = Services
    fields = ["category", "services", "description", "price"]

    def form_valid(self, form):
        form.save()
        form.instance.provider.add(self.request.user.pk)
        return super(ServiceCreationView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('providers:service_list')

class ServiceListView(LoginRequiredMixin, ListView):
    model = Services

    def get_queryset(self):
        provider =  self.request.user.serviceproviders.pk
        return Services.objects.filter(provider=provider)
        