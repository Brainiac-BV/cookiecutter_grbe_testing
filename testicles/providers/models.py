from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

from enum import Enum
from .managers import ProviderServiceManager
# Create your models here.

class ServiceProviders(models.Model):
    # Inheriting methods from user, using to extend for providers
    # Get user info from user app
    user_info = models.OneToOneField(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        primary_key=True, 
        )
    zip_code = models.IntegerField(unique=True, )
    # Used for Profile page
    date_joined = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=80)
    about_me = models.TextField(verbose_name='About Me', max_length=300, 
    help_text='Tell them about yourself! Why should they choose you? What makes you stand out?',
    )
    header_img = models.ImageField(verbose_name="Profile Header Image", blank=True, null=True)
    is_licensed = models.BooleanField('Have You aquired any beauticians license?', default=False)
    
    CATEGORIES = (
        ('Hair', 'Hair'),
        ('Nails', 'Nails'),
        ('Face', 'Face'))
    
    service_categories = models.CharField(max_length=40, choices=CATEGORIES )
    services =  models.ManyToManyField('Services')

    def _get_full_name(self):
        # Returns the person's full name."
        return '%s' % (self.user_info.username)
    name = property(_get_full_name)
    
    """
    def _get_services(self):
        # Returns the providers associated services."
        results = Services.objects.filter(provider=self).order_by('category')
        services = ""
        for res in results:
            services += '%s - %s ' %  (res.category, res.services)
        return services
    services_list = property(_get_services)
    """
    def __str__(self):
        return self.name

class Services(models.Model):
    """
    This model class exists
     to contain all of the available services providers will be able to choose 
    from on their profile pages, which will also be in search filtering, appointment creation and
    in read only view when customers view a provider profile.
    """
    CATEGORIES = (
    ('Hair', 'Hair'),
    ('Nails', 'Nails'),
    ('Make Up', 'Make up'))
    
    category = models.CharField(max_length=20, choices=CATEGORIES)

    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=40)
    #provider = models.ManyToManyField('ServiceProviders',)
    
    def __str__(self):
        return self.name

"""
class SubServices(models.Model):
    
    This model class exists to contain all of the available secondary services which will be associated with 
    a primary service. Providers will be able to choose from on their profile pages, which will also be in search 
    filtering, appointment creation and in read only view when customers view a provider profile.
       
    hair_choices = ArrayField(models.CharField(max_length=20, blank=True, null=True, default='wtf do i have to do here'))
    nail_choices = ArrayField(models.CharField(max_length=20, blank=True, null=True, default='wtf do i have to do here'))
    makeup_choices = ArrayField(models.CharField(max_length=20))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Appointments(models.Model):
    
    This model class exists to contain all of the available appointments providers will be able to  
    view on profile pages (read only), users will request these through a form on providers page.
      
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_datetime = models.DateTimeField(auto_now_add=True)
    requesting_user = models.ManyToManyField(settings.AUTH_USER_MODEL,)
                            #related_name='name')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
"""

class ProviderRequests(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField()
    #category = models.ForeignKey(Services, on_delete='CASCADE', )
    services = models.CharField(max_length=20)
    requesting_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete='CASCADE',
                                        to_field='username',
    )
    provider = models.ForeignKey('ServiceProviders', on_delete='CASCADE')
    created = models.DateTimeField(auto_now_add=True, blank=True)
    accepted = models.NullBooleanField()

    def __str__(self):
        return self.requesting_user

    def __unicode__(self):
        return self.requesting_user.name

    def get_absolute_url(self):
        return reverse("providers:provider_request" )
