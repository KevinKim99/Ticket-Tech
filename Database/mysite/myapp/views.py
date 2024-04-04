from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import Artists
from .models import Concerts, Artists, client, payment, myTickets
from .forms import SignUpForm
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

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

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Hash the password
        hashed_password = make_password(password)
        # Create a new client object with hashed password and save it to the database
        new_client = client(name=username, email=email, password=hashed_password)
        new_client.save()
        return redirect('login')  # Redirect to the login page after signup
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        # Authenticate user
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            # User authenticated, log in user
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            # Authentication failed, handle error
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def get_artists(request):
    try:
        # Fetch all artists from the database
        artists = Artists.objects.all().values('ArtistName', 'ArtistImage')
        return JsonResponse(list(artists), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def get_client(request):
    try:
        clients = client.objects.all().values('name','email','password')
        return JsonResponse(list(clients), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def get_payment(request):
    try:
        payments = payment.objects.all().values('paymentType','address','postalCode')
        return JsonResponse(list(payments), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def addArtist(ArtistId, ArtistName, ArtistImage):
    artist = Artists(ArtistId=ArtistId, ArtistName=ArtistName, ArtistImage=ArtistImage)
    artist.save()
    
def concerts_view(request):
    concerts = Concerts.objects.all()
    artists = Artists.objects.all()
    return render(request, 'Concerts.html', {'concerts': concerts, 'artists': artists})

def logout_view(request):
    logout(request)
    return redirect('home')