from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'


'debug' => env('APP_DEBUG', false)