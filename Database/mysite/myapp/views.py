from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import Concerts
from .models import Artists


# Create your views here.


def home(request):
    return render(request, "home.html")

def concerts_view(request):
    return render(request, 'Concerts.html')

def todos(request):
    items = TodoItem.objects.all
    return render(request, "todos.html", {"todos": items})

def concerts(request):
    items = Concerts.objects.all
    return render(request, "Concerts.html", {"concerts": items})

def artists(request):
    items = Artists.objects.all
    return render(request, "Artists.html", {"artistNames": items})


def addConcert(ConcertId, ArtistId, ConcertDate, Venue, City, TicketQuantity, TicketPrice):
    concert = Concerts(ConcertId = ConcertId, ArtistId = ArtistId, ConcertDate = ConcertDate, Venue = Venue, City = City, TicketQuantity = TicketQuantity, TicketPrice = TicketPrice)
    concert.save()


def addArtist(ArtistId, ArtistName, ArtistImage):
    artist = Artists(ArtistId = ArtistId, ArtistName = ArtistName, ArtistImage = ArtistImage)
    artist.save()


#TODO Add all artists and concerts
addArtist(3, "The Funky Monkeys", "https://drive.google.com/file/d/11AxDiz6NpGn4X60yPmuJMe85alfaS-LW/view?usp=sharing")

