from django.shortcuts import render
from .models import History, TitleHistory


def home(request):
    context = {'TitleHistory': TitleHistory.objects.all(), 'history': History.objects.all()}
    template = 'home.html'
    return render(request, template, context)



