from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Pages


class ActionPublish(admin.ModelAdmin):
    """Action для публикации и снятия с публикации"""

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    def publish(self, request, queryset):
        """Опубликовать"""
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)


class PagesAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    text = forms.CharField(required=False, label="Контент страницы", widget=CKEditorUploadingWidget())

    class Meta:
        model = Pages
        fields = '__all__'


@admin.register(Pages)
class PagesAdmin(ActionPublish):
    """Статичные страницы"""
    list_display = ("title", "published", "id")
    list_editable = ("published", )
    list_filter = ("published", "template")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title", )}
    form = PagesAdminForm
    actions = ['unpublish', 'publish']
    save_on_top = True
    # readonly_fields = ("slug",)

