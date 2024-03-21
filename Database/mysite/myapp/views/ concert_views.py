from django.shortcuts import render, HttpResponse
from ..models import Concerts


def concerts_view(request):
   return render(request, 'Concerts.html')


def concerts(request):
   items = Concerts.objects.all
   return render(request, "Concerts.html", {"concerts": items})