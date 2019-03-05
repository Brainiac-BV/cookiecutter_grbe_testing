from django.shortcuts import render

from .models import ServiceProviderForm
# Create your views here.

def provider_view(request):
    form = ServiceProviderForm()
    return render(request, 'providers/form.html', {'form':form} )   