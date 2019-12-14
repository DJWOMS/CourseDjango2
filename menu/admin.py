from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# from utils.admin import ActionPublish
from .models import Menu, MenuItem
from .forms import MenuItemAdminForm


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Меню"""
    list_display = ("name", "status", "published")
    list_filter = ("published",)
    #actions = ['unpublish', 'publish']


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    """Пункты меню"""
    #form = MenuItemAdminForm
    list_display = ("title", "name", "parent", "menu", "sort", "published")
    list_filter = ("menu", "parent", "published")
    search_fields = ("name", "parent__name", "menu__name")
    save_as = True
    list_editable = ("sort", "published")
    mptt_level_indent = 20
    #actions = ['unpublish', 'publish']

