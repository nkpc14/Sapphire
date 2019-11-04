from django.db import models


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    discription = models.CharField(max_length=1000)
    tagline = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    fee = models.FloatField()
    poster = models.ImageField()
    image = models.ImageField()

    def __str__(self):
        return self.name
