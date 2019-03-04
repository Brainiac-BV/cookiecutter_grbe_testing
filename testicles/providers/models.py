from django.db import models


from django.contrib.postgres.fields import ArrayField

# Create your models here.

class ServiceProvider(models.Model):
    # Inheriting methods from user, using to extend for providers
    '''
    AVAILABLE_SERVICES = (
        ('h', 'hair styling'),
        ('n', 'nail styling'),
        ('m', 'makeup styling'),
    )
    '''
    # Get user info from user app
    user_info = models.OneToOneField('users.User', 
        on_delete='cascade',
        blank=True, null=True,
        )
    # Used to display services a provider chooses from Services
    services_provided = models.ManyToManyField('Services',
        help_text='select the services you would like to provide',
    )


class Services(models.Model):
    name = ArrayField(models.CharField(max_length=20))
    date_added = models.DateTimeField(auto_now_add=True)