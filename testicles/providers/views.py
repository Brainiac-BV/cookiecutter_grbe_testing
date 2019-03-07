from django.shortcuts import render
from django.views.generic import UpdateView, ListView


from .models import ServiceProviders
# Create your views here.

'''
def provider_view(request):
    form = ServiceProviderForm()
    return render(request, 'providers/form.html', {'form':form} )   
'''

class ProviderView(UpdateView):
    model = ServiceProviders
    slug_field = "username"
    slug_url_kwarg = "username"


provider_view = ProviderView.as_view()

class ProviderListView(ListView):
    model = ServiceProviders
    slug_field = "username"
    slug_url_kwarg = "username"


provider_list_view = ProviderListView.as_view()