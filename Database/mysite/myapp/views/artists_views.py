from django.shortcuts import render, HttpResponse
from ..models import Artists


def artists(request):
   items = Artists.objects.all
   return render(request, "Artists.html", {"artistNames": items})


def addArtist(ArtistId, ArtistName, ArtistImage):
   artist = Artists(ArtistId = ArtistId, ArtistName = ArtistName, ArtistImage = ArtistImage)
   artist.save()
  
#TODO Add all artists
addArtist(3, "The Funky Monkeys", "https://drive.google.com/file/d/11AxDiz6NpGn4X60yPmuJMe85alfaS-LW/view?usp=sharing")