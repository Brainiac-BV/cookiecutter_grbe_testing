from django.db import models

class ProviderServiceManager(models.Manager):
    def get_service_by_provider(self, keyword):
        return self.filter(provider=keyword)