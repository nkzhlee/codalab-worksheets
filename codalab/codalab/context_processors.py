from django.conf import settings
from codalab import settings as codalab_settings


def app_version_proc(request):
    "A context processor that provides 'app_version'."
    return {
        'CODALAB_VERSION': settings.CODALAB_VERSION,
    }

def common_settings(request):
    "A context processor that returns dev settings"
    return {}
