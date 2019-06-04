from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from providers import models as provider_model


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    is_provider = models.BooleanField(
        verbose_name="Service Provider Status",
        default=False
        )

    profile_pic = models.ImageField(upload_to="images", 
                    max_length=100, blank=True, null=True)

    #payment_info = 
    
    def is_service_provider(self):
        return self.is_provider

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


