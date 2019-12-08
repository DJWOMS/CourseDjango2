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
    list_display = ("title", "name", "parent", "menu", "sort", "id", "published")
    list_filter = ("menu", "parent", "published")
    search_fields = ("name", "parent", "menu")
    save_as = True
    list_editable = ("sort", )
    mptt_level_indent = 20
    #actions = ['unpublish', 'publish']

