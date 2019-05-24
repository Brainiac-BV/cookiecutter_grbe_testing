from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView, CreateView, FormView, TemplateView
from django.views import View
from django.core.mail import send_mail
from allauth.account.models import EmailAddress

from postman.api import pm_write


from .models import ServiceProviders, ProviderRequests, Services
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
        context['form'] = RequestForm()
        return context

provider_detail_view = ProviderDetailView.as_view()

class ProviderRequestFormView(CreateView):
    form_class = RequestForm
    model = ProviderRequests


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


class ProviderRequestFormList(ListView):
    model = ProviderRequests

    def get_queryset(self):
        """ Returns requests based on logged in provider_id"""
        provider = self.request.user.serviceproviders.pk
        return ProviderRequests.objects.filter(provider_id=provider).order_by('start_date')

class ProviderRequestDecison(UpdateView):
    model = ProviderRequests
    fields = ['accepted', ]
    template_name = "providers/request_decision.html"
   
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.GET.get('username')
        email2 = ProviderRequests.objects.get(requesting_user_id=user)
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
    
class ProviderDashboard(DetailView):
    model = ServiceProviders
    slug_field = "user_info"
    slug_url_kwarg = "user_info"
    template_name = "providers/serviceprovider_dash.html"
    