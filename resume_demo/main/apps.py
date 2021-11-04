from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
<<<<<<< HEAD
    def ready(self):
        import main.signals
=======

    # def ready(self):
    #     import main.signals
>>>>>>> 4c172ba2443b21df26bae70408de9b09d1957031
