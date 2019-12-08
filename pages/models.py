from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _


class Pages(models.Model):
    """Страницы"""
    title = models.CharField(_("Заголовок"), max_length=500)
    sub_title = models.CharField(_("Подзаголовок"), max_length=500, blank=True, null=True)
    text = models.TextField(_("Текст"), blank=True, null=True)
    edit_date = models.DateTimeField(
        _("Дата редактирования"),
        auto_now=True,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(_("Дата публикации"), blank=True, null=True)
    published = models.BooleanField(_("Опубликовать?"), default=True)
    template = models.CharField(_("Шаблон"), max_length=500, default="pages/home.html")
    registration_required = models.BooleanField(
        _('Требуется регистрация'),
        help_text=_("Если флажок установлен, только зарегистрированные пользователи могут "
                    "просматривать страницу."),
        default=False,
    )
    slug = models.CharField("url", max_length=100, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = "/"
        if not f"{self.slug}".startswith("/"):
            self.slug = "/" + self.slug
        if not self.slug.endswith("/"):
            self.slug += "/"
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return iri_to_uri(get_script_prefix().rstrip('/') + self.slug)

    class Meta:
        verbose_name = _("Страница")
        verbose_name_plural = _("Страницы")
        unique_together = ('slug',)


