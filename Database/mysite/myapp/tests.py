from django.test import TestCase
from .views import addConcert
from .views import addArtist
from .views import addClient
from .views import addPayment
from .views import addMyTickets
from .models import Artists
from .models import Concerts
from .models import client
from .models import payment
from .models import myTickets

# Create your tests here.


class AddArtistTest(TestCase):
    def test_add_artist(self):
        # Add a new artist
        addArtist(100, 'BandName', "BandImage")
        
        # Check if the artist was added correctly
        artist = Artists.objects.get(name='Artist Name')
        self.assertEqual(artist.ArtistName, 'BandName')


class AddConcertTest(TestCase):
    def test_add_concert(self):
        #Add a new concert
        addConcert(1000, 1000, )

class AddClient(TestCase):
    def test_add_client(self):
        addClient(0, "Kevin", "aaaa111@gmail.com", "ASqw1212")

class AddPayment(TestCase):
    def test_add_payment(self):
        addPayment(0, 0, "Visa", "802Academy", "V1V3A4")

class AddMyTickets(TestCase):
    def test_add_my_tickets(self):
        addMyTickets(1,1,1)