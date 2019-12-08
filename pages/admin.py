# from django import forms
from django.contrib import admin
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
#
#
from .models import Pages

admin.site.register(Pages)

#
# class PagesAdminForm(forms.ModelForm):
#     """Виджет редактора ckeditor"""
#     text = forms.CharField(required=False, label="Контент страницы", widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = Pages
#         fields = '__all__'
#
#
# class BlockPageForm(forms.ModelForm):
#     """Виджет редактора ckeditor"""
#     description = forms.CharField(required=False, label="Описание", widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = BlockPage
#         fields = '__all__'
#
#
# class BlockPageAdmin(admin.StackedInline):
#     model = BlockPage
#     extra = 1
#     form = BlockPageForm
#
#
# @admin.register(Pages)
# class PagesAdmin(ActionPublish):
#     """Статичные страницы"""
#     list_display = ("title", "lang", "published", "id")
#     list_editable = ("published", )
#     list_filter = ("published", "lang", "template")
#     search_fields = ("title",)
#     prepopulated_fields = {"slug": ("title", )}
#     form = PagesAdminForm
#     actions = ['unpublish', 'publish']
#     inlines = [SeoInlines, BlockPageAdmin]
#     save_on_top = True
#     readonly_fields = ("get_slug_url",)
#
#
#
#
