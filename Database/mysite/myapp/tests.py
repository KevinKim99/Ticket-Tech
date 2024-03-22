
from django.test import TestCase
from django.shortcuts import render, HttpResponse
from .views import addConcert
from .views import addArtist
from .views import removeArtist
from .views import removeConcert
from .models import Artists
from .models import Concerts

# Create your tests here.

class TestAddArtist(TestCase):
    def test_add_artist(self):
        # Add a new artist
        addArtist(100, "BandName", "BandImage")
        
        # Check if the artist was added correctly
        artist = Artists.objects.get(ArtistName='BandName')
        self.assertEqual(artist.ArtistName, 'BandName')


class TestRemoveArtist(TestCase):
    def setUp(self):
        # Add a new artist to the database
        self.artist = Artists.objects.create(ArtistId = 1000, ArtistName='BandName', ArtistImage="BandImage")

    def test_remove_artist(self):
        # Ensure that the artist exists before removal
        self.assertTrue(Artists.objects.filter(ArtistName='BandName').exists())

        # Remove the artist
        removeArtist(self.artist.ArtistId)

        # Check if the artist is removed from the database
        self.assertFalse(Artists.objects.filter(ArtistId = 1000).exists())

    def test_remove_nonexistent_artist(self):
        # Try removing an artist that doesn't exist
        result = removeArtist(999)
        self.assertFalse(result)


class TestAddConcert(TestCase):
    #add concert
    def test_add_new_concert(self):
        addConcert(1000, 100, '2020-08-08', 'Sample Venue', 'Sample City', 500, 50.00)
     
        #verify concert was added
        concert = Concerts.objects.get(ConcertId = 1000)
        self.assertEqual(concert.ConcertId, 1000)

    def test_add_concert_without_artist(self):
        # Try adding a concert without specifying an artist
        with self.assertRaises(ValueError):
            addConcert(1001, None, '2020-08-08', 'Sample Venue', 'Sample City', 500, 50.00)
    
class TestRemoveConcert(TestCase):
    def setUp(self):
        #add a concert to remove
        self.concert = Concerts.objects.create(ConcertId = 1000, ArtistId = 100, ConcertDate = '2020-08-08', Venue = 'Sample Venue', City = 'sample City', TicketQuantity = 500, TicketPrice = 50.00)

    def test_remove_concert(self):
        # Ensure that the concert exists before removal
        self.assertTrue(Concerts.objects.filter(ConcertId=1000).exists())

        #remove the Concert
        removeConcert(self.concert.ConcertId)

        #verify it was removed
        self.assertFalse(Concerts.objects.filter(ConcertId = 1000).exists())

    def test_remove_nonexistent_concert(self):
        # Try removing a concert that doesn't exist
        result = removeConcert(999)
        self.assertFalse(result)
        
class TestAddArtist(TestCase):
    def test_add_artist(self):
        # Add a new artist
        addArtist(100, "BandName", "BandImage")
        
        # Check if the artist was added correctly
        artist = Artists.objects.get(ArtistName='BandName')
        self.assertEqual(artist.ArtistName, 'BandName')


class TestRemoveArtist(TestCase):
    def setUp(self):
        # Add a new artist to the database
        self.artist = Artists.objects.create(ArtistId = 1000, ArtistName='BandName', ArtistImage="BandImage")

    def test_remove_artist(self):
        # Ensure that the artist exists before removal
        self.assertTrue(Artists.objects.filter(ArtistName='BandName').exists())

        # Remove the artist
        removeArtist(self.artist.ArtistId)

        # Check if the artist is removed from the database
        self.assertFalse(Artists.objects.filter(ArtistId = 1000).exists())

class TestAddConcert(TestCase):
    #add concert
    def test_add_new_concert(self):
        addConcert(1000, 100, '2020-08-08', 'Sample Venue', 'Sample City', 500, 50.00)
     
     #verify concert was added
        concert = Concerts.objects.get(ConcertId = 1000)
        self.assertEqual(concert.ConcertId, 1000)
    
class TestRemoveConcert(TestCase):
    def setUp(self):
        #add a concert to remove
        self.concert = Concerts.objects.create(ConcertId = 1000, ArtistId = 100, ConcertDate = '2020-08-08', Venue = 'Sample Venue', City = 'sample City', TicketQuantity = 500, TicketPrice = 50.00)

    def test_remove_concert(self):
        # Ensure that the concert exists before removal
        self.assertTrue(Concerts.objects.filter(ConcertId=1000).exists())

        #remove the Concert
        removeConcert(self.concert.ConcertId)

        #verify it was removed
        self.assertFalse(Concerts.objects.filter(ConcertId = 1000).exists())