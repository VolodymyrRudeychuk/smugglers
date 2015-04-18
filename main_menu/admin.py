from django.contrib import admin

from main_menu.models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Menu, MenuAdmin)