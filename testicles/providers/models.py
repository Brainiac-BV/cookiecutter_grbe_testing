from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField


from users.models import User



# Create your models here.

class ServiceProviders(models.Model):
    # Inheriting methods from user, using to extend for providers
    # Get user info from user app
    user_info = models.OneToOneField(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        blank=True,
        primary_key=True,
        )
    
    def get_username(self):
        return self.user_info.username
         
    DEFAULT_CHOICE = "No Services"
    
    AVAILABLE_SERVICES = (
        ('hair', 'hair styling'),
        ('nails', 'nail styling'),
        ('makeup', 'makeup styling'),
    )

    # Used to display services a provider chooses from AVAILABLE_SERVICES
    services_chosen = ArrayField(models.CharField(max_length=10,
                                 choices=AVAILABLE_SERVICES, 
                                 default=DEFAULT_CHOICE,))

    #dates_available = models.DateTimeField(blank=True, null=True)        
    
    #def __str__(self)
    '''
    services_provided = models.ManyToManyField('Services',
        help_text='select the services you would like to provide',
    )
    '''

'''
class Services(models.Model):
    name = ArrayField(models.CharField(max_length=20))
    date_added = models.DateTimeField(auto_now_add=True)
    
'''

