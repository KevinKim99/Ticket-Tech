from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)


class Concerts(models.Model):
    ConcertId = models.IntegerField
    ArtistId = models.IntegerField
    ConcertDate = models.DateTimeField
    Venue = models.CharField(max_length = 255)
    City = models.CharField(max_length = 255)
    TicketQuantity = models.IntegerField
    TicketPrice = models.FloatField
