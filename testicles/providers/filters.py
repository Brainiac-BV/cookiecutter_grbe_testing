from django import forms
import django_filters

from .models import Services

class ServicesFilter(django_filters.FilterSet):
    services = django_filters.ModelMultipleChoiceFilter(queryset=Services.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Services
        fields = ("services", "category",)