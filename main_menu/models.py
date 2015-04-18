from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=25)
    url = models.CharField(max_length=255)