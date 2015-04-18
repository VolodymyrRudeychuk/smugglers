from django.contrib import admin
from .models import History, TitleHistory
from .models import Beer
from django.contrib import messages
from django.forms import ModelForm, ValidationError
from easy_maps.widgets import AddressWithMapWidget
from .models import Map, Message
from .models import Social
from .models import LastNews
from .models import BeerTitle
from .models import AgeModal


class AgeModalAdmin(admin.ModelAdmin):
    list_display = ('title',)


class BeerTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_small')


class LastNewsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class SocialAdmin(admin.ModelAdmin):
    list_display = ('title', 'facebook', 'twitter', 'youtube')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'date')
    readonly_fields = ('name', 'email', 'phone', 'message', 'date')


class TitleHistoryForm(ModelForm):
    model = TitleHistory

    def clean(self):
        if self.model.objects.count() > 1:
            raise ValidationError('Only one item can be added for history title')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "pictures", "text",)


class TitleHistoryAdmin(admin.ModelAdmin):
    list_display = ("head_title", "head_slug")
    form = TitleHistoryForm


admin.site.register(TitleHistory, TitleHistoryAdmin)
admin.site.register(History, HistoryAdmin)


class BeerAdmin(admin.ModelAdmin):
    list_display = ("beer_pic", "beer_title", "beer_slug")


admin.site.register(Beer, BeerAdmin)

MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success success',
    messages.WARNING: 'alert-warning warning',
    messages.ERROR: 'alert-danger error'

}


class MapAdmin(admin.ModelAdmin):
    list_display = ('address', )


# class Admin(admin.ModelAdmin):
# class form(forms.ModelForm):
#         class Meta:
#             widgets = {
#                 'address': AddressWithMapWidget({'class': 'vTextField'})
#             }
#
admin.site.register(Map, MapAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(LastNews, LastNewsAdmin)
admin.site.register(BeerTitle, BeerTitleAdmin)
admin.site.register(AgeModal, AgeModalAdmin)