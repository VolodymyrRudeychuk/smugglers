from django.contrib import admin
from .models import History, TitleHistory


class HistoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "pictures", "text",)

admin.site.register(History, HistoryAdmin)

class TitleHistoryAdmin(admin.ModelAdmin):
    list_display = ("head_title", "head_slug")

admin.site.register(TitleHistory, TitleHistoryAdmin)