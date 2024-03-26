from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import Concerts
from .models import Artists

from .models import client
from .models import payment
from .models import myTickets
from django.shortcuts import render, redirect
from .forms import SignUpForm

from django.core.exceptions import ObjectDoesNotExist




# Create your views here.


def home(request):
    return render(request, "home.html")

def concerts_view(request):
    return render(request, 'Concerts.html')

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


def addClient(id, name, email, password):
    client2 = client(id = id, name = name, email = email, password = password)
    client2.save()

def addPayment(id, userId, paymentType, address, postalCode):
    payment2 = payment(id = id, userId = userId, paymentType = paymentType, address = address, postalCode = postalCode)
    payment2.save()

def addMyTickets(id, userId, concertId):
    myTicket2 = myTickets(id = id, userId = userId, concertId = concertId)
    myTicket2.save()
    
def removeArtist(artist_id):
    try:
        # Attempt to get the artist from the database
        artist = Artists.objects.get(pk=artist_id)
    except ObjectDoesNotExist:
        # If the artist does not exist, return False
        return False
    
    # Delete the artist
    artist.delete()
    return True


def removeConcert(concert_id):
    try:
        # Attempt to get the concert from the database
        concert = Concerts.objects.get(pk=concert_id)
    except ObjectDoesNotExist:
        # If the concert does not exist, return False
        return False
    
    # Delete the concert
    concert.delete()
    return True

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')  # Redirect to the login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



#TODO Add all artists and concerts
addArtist(3, "The Funky Monkeys", "https://drive.google.com/file/d/11AxDiz6NpGn4X60yPmuJMe85alfaS-LW/view?usp=sharing")

