from django.apps import AppConfig


class WelcomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "apps.welcome"
