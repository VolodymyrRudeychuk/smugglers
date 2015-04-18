from django.shortcuts import render
from .models import (
    History,
    TitleHistory,
    Message,
    Map,
    Beer,
    Social,
    LastNews,
    BeerTitle,
    AgeModal
)
from news.models import Entry
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm



class MessageForm(ModelForm):
    class Meta:
        model = Message


def home(request):
    context = {'title_history': TitleHistory.objects.all(),
               'history': History.objects.all(),
               'beers': Beer.objects.all(),
               'map': Map.objects.first(),
               'feed': Entry.objects.all().order_by('-id')[:2],
               'social': Social.objects.first(),
               'last': LastNews.objects.first(),
               'beertitle': BeerTitle.objects.first(),
               'howage': AgeModal.objects.first(),
                }
    template = 'home.html'
    return render(request, template, context)


@csrf_exempt
def send_email(request):
    print request.POST
    form = MessageForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('Good boy!')
    else:
        return HttpResponseBadRequest('Bad boy!')





