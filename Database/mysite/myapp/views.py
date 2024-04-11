from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import Artists
from .models import Concerts, Artists, client, payment, myTickets, cart
from .forms import SignUpForm
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib import messages

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

def addMyTickets(id, userId, concertId, ticketPrice, ticketSection):
    myTicket2 = myTickets(id = id, userId = userId, concertId = concertId, ticketPrice = ticketPrice, ticketSection= ticketSection)
    myTicket2.save()
    
def addCart(userId, concertId):
    cart2 = cart(userId = userId, concertId = concertId)
    cart2.save()
    
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
    # Check if the user is already logged in
    if request.session.get('user_id'):
        return redirect('userPage')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = client.objects.get(name=username)
            if check_password(password, user.password):
                # Correct password, log the user in by setting the session
                request.session['user_id'] = user.id
                # Optionally, store more information in the session
                request.session['user_name'] = user.name
                return redirect('userPage')  # Redirect to a user-specific page
            else:
                # Incorrect password
                messages.error(request, "Invalid username or password.")
        except client.DoesNotExist:
            # Username does not exist
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def get_artists(request):
    try:
        # Fetch all artists from the database
        artists = Artists.objects.all().values('ArtistName', 'ArtistImage','ArtistId')
        return JsonResponse(list(artists), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_concerts(request):
    try:
        # Fetch all concerts from the database
        concerts = Concerts.objects.all().values('ConcertId', 'ArtistId','ConcertDate','Venue','City','TicketQuantity','TicketPrice')
        return JsonResponse(list(concerts), safe=False)
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

def artist_details_view(request, artist_name):
    artist = get_object_or_404(Artists, ArtistName=artist_name)
    concerts = Concerts.objects.filter(ArtistId=artist.ArtistId)
    return render(request, 'Details.html', {'artist': artist, 'concerts': concerts})

def search_results_view(request):
    query = request.GET.get('q', '')
    print("Search Query:", query)  # Debugging
    keywords = query.split()
    artists = Artists.objects.none()
    for keyword in keywords:
        artists |= Artists.objects.filter(ArtistName__icontains=keyword)
    
    processed_artists = []
    for artist in artists:
        image_id = extract_image_id(artist.ArtistImage)
        processed_artists.append({'artist': artist, 'image_id': image_id})
    
    print("Matching Artists:", processed_artists)  # Debugging
    return render(request, 'search-results.html', {'artists': processed_artists})

def extract_image_id(image_url):
    # a weird way of doing things but it works
    #index of '/d/' which marks the start of the image ID
    key_start_index = image_url.find('/d/') + 3
    #index of '/view' which marks the end of the image ID
    key_end_index = image_url.find('/view')
    # Extract the image ID from the URL
    image_id = image_url[key_start_index:key_end_index]
    return image_id

def logout_view(request):
    request.session.flush()  # Clears all session data
    return redirect('home')  # Redirect to the homepage or login page