from django.test import TestCase
from .views import addConcert
from .views import addArtist
from .models import Artists
from .models import Concerts
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

