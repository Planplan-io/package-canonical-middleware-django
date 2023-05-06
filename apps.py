from django.apps import AppConfig
from django.conf import settings
from django.core.checks import Error, Tags, Warning, register


class PackageCanonicalMiddlewareDjangoAppConfig(AppConfig):
    name = "package-canonical-middleware-django"

    def ready(self):
        register(Tags.security)(default_checks)
        register(Tags.security, deploy=True)(deploy_checks)
