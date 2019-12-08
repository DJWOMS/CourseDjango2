from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PagesConfig(AppConfig):
    name = 'pages'
    verbose_name = _('Страницы')
