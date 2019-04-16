from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from providers import models as provider_model


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    zip_code = models.IntegerField(blank=True, null=True)
    service_provider_status = models.BooleanField(
        verbose_name="Service Provider Status",
        default=False
        )
    #provider_info = models.ManyToManyField('providers.ServiceProvider')
    profile_pic = models.ImageField(upload_to="images", 
                    max_length=100, blank=True, null=True)
    
    # appointments scheduled by user. Used to link user to appt and on the other side appt to provider
    #appointments = 

    def is_service_provider(self):
        return self.service_provider_status

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


