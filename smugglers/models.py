from django.db import models


class History(models.Model):

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=150, blank=True)
    pictures = models.ImageField("")
    text = models.TextField()


    class Meta:
        ordering = ('-id', )


class TitleHistory(models.Model):
        head_title = models.CharField(max_length=100, blank=True)
        head_slug = models.CharField(max_length=100, blank=True)