from django.shortcuts import render, HttpResponse
from ..models import TodoItem
from ..models import Concerts
from ..models import Artists
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
   return render(request, "home.html")


def login_view(request):
   return render(request, 'login.html')


def Details_view(request):
   return render(request, 'Details.html')


def cart_view(request):
   return render(request, 'cart.html')


def searchform_view(request):
   return render(request, 'search-form.html')


def searchresults_view(request):
   return render(request, 'search-results.html')


def signup_view(request):
   return render(request, 'signup.html')


def userPage_view(request):
   return render(request, 'userPage.html')
