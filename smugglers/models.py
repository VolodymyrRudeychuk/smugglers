from django.db import models
from geopy.geocoders import Nominatim


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


class Beer(models.Model):
    beer_title = models.CharField(max_length=20, blank=True)
    beer_slug = models.CharField(max_length=20, blank=True)
    beer_text = models.TextField(blank=True)
    beer_pic = models.ImageField("")


class Map(models.Model):
    title = models.CharField(max_length=100, blank=True)
    mini_title = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    long = models.FloatField(default=None, null=True, editable=False)
    lang = models.FloatField(default=None, null=True, editable=False)
    zoom = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        geolocator = Nominatim(timeout=3)
        location = geolocator.geocode(self.address)
        self.address = location.address
        self.long = location.latitude
        self.lang = location.longitude
        super(Map, self).save(*args, **kwargs)


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Social(models.Model):
    title = models.CharField(max_length=30)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)


class LastNews(models.Model):
    title = models.CharField(max_length=30)


class BeerTitle(models.Model):
    title = models.CharField(max_length=100)
    title_small = models.CharField(max_length=100)


class AgeModal(models.Model):
    title = models.CharField(max_length=200)