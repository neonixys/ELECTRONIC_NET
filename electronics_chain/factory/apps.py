from django.apps import AppConfig


class FactoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'electronics_chain.factory'
    verbose_name = 'Завод'
