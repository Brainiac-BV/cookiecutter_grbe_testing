from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

from enum import Enum

# Create your models here.

class ServiceProviders(models.Model):
    # Inheriting methods from user, using to extend for providers
    # Get user info from user app
    user_info = models.OneToOneField(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        primary_key=True, 
        )

    #dates_available = models.DateTimeField(blank=True, null=True)        
    
    services_provided = models.ManyToManyField('Services', 
                        help_text='select the services you would like to provide',
    )

    # Used for Profile page
    about_me = models.TextField(verbose_name='About Me', max_length=300, 
    help_text='Tell them about yourself! Why should they choose you? What makes you stand out?',
    default='Fuck It'
    )
    
    # Associate appointments with chosen provider
    #appointments = models.ManyToManyField('Appointments')

class Services(models.Model):
    """
    This model class exists to contain all of the available services providers will be able to choose 
    from on their profile pages, which will also be in search filtering, appointment creation and
    in read only view when customers view a provider profile.
    """
    SUB_CHOICES = (
    ('Hair', (
            ('braiding', 'braiding'),
            ('cut', 'cut'),
            ('w/d', 'Wash and dry'),
            ('styling', 'styling'),
        )
    ),
    ('Nails', (
            ('natural', 'Natural Set'),
            ('full', 'Full Set'),
        )
    ),
    ('Make up', (
            ('full_face', 'Full Face'),
            ('touchup', 'Touchup'),
        )
)
)
    name = ArrayField(models.CharField(max_length=20))

    sub_choice = models.CharField(
                max_length=20,
                choices=SUB_CHOICES,
                default='Hair',)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.name[0]

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

class Request(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField()
    requested_service = models.ForeignKey('Services', on_delete='CASCADE')
    sub_service = models.CharField(max_length=25, choices=Services.SUB_CHOICES, blank=True, null=True)
    requesting_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete='CASCADE',
                                        to_field='username',
    )
    provider = models.ForeignKey('ServiceProviders', on_delete='CASCADE')
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.requesting_user

    def __unicode__(self):
        return self.requesting_user.name

    def get_absolute_url(self):
        return reverse("providers:request")
