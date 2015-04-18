
from django.views import generic
from . import models
from django.http import HttpResponse



class BlogIndex(generic.ListView):

    queryset = models.Entry.objects.published()
    template_name = "newshome.html"
    paginate_by = 3


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"
