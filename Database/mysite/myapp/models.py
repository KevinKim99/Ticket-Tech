from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)


class Concerts(models.Model):
    ConcertId = models.AutoField(primary_key = True)
    ArtistId = models.IntegerField()
    ConcertDate = models.DateTimeField()
    Venue = models.CharField(max_length = 255)
    City = models.CharField(max_length = 255)
    TicketQuantity = models.IntegerField()
    TicketPrice = models.DecimalField(max_digits=7, decimal_places = 2)

class Artists(models.Model):
    ArtistId = models.IntegerField(primary_key=True)
    ArtistName = models.CharField(max_length = 255)
    ArtistImage = models.CharField(max_length = 255)


class client(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)

class payment(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    paymentType = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    postalCode = models.CharField(max_length = 255)

class myTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    concertId = models.IntegerField()
    ticketPrice = models.IntegerField(default=0)
    ticketSection = models.IntegerField(default=0)


class cart(models.Model):
    userId = models.IntegerField()
    concertId = models.IntegerField()