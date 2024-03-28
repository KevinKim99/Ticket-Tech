from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import Concerts
from .models import Artists

from .models import client
from .models import payment
from .models import myTickets
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse





# Create your views here.


def home(request):
    return render(request, "home.html")

def concerts_view(request):
    return render(request, 'Concerts.html')

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

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import client

def signup_view(request):
    # Handle signup logic here
    return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Create a new Client object and save it to the database
        new_client = client(name=username, email=email, password=password)
        new_client.save()
        return redirect('login_view')  # Redirect to the login page after signup
    return render(request, 'signup.html')

def login_view(request):
    # Handle login logic here
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if the provided email and password match any client in the database
        try:
            matched_client = client.objects.get(email=email, password=password)
            # Perform login logic here, such as setting session variables
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        except client.DoesNotExist:
            # Handle invalid credentials, e.g., display an error message
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})
    return render(request, 'login.html')


def get_artists(request):
    try:
        # Fetch all artists from the database
        artists = Artists.objects.all().values('ArtistName', 'ArtistImage')
        return JsonResponse(list(artists), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def addArtist(ArtistId, ArtistName, ArtistImage):
    artist = Artists(ArtistId=ArtistId, ArtistName=ArtistName, ArtistImage=ArtistImage)
    artist.save()
    
def concerts_view(request):
    concerts = Concerts.objects.all()
    artists = Artists.objects.all()
    return render(request, 'Concerts.html', {'concerts': concerts, 'artists': artists})


from django.shortcuts import render, get_object_or_404
from .models import Artists

def artist_details_view(request, artist_name):
  # get artists name from db
    artist = get_object_or_404(Artists, ArtistName=artist_name)
    
    # essentially our sql join 
    concerts = Concerts.objects.filter(ArtistId=artist.ArtistId)
    # render this shit, details table and concerts table
    return render(request, 'details.html', {'artist': artist, 'concerts': concerts})

#TODO Add all artists and concerts
addArtist(3, "The Funky Monkeys", "https://drive.google.com/file/d/11AxDiz6NpGn4X60yPmuJMe85alfaS-LW/view?usp=sharing")


