from django.apps import AppConfig


class FrsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FRS'
    # def ready(self):
    #     import FRS.signals
