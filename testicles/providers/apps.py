from django.apps import AppConfig


class ProvidersConfig(AppConfig):
    name = 'providers'
    verbose_name = 'Providers'

    def ready(self):
        try:
            import providers.signals  # noqa F401
        except ImportError:
            pass
