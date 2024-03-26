
from django.test import TestCase
from django.shortcuts import render, HttpResponse
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


class AddClient(TestCase):
    def test_add_client(self):
        addClient(0, "Kevin", "aaaa111@gmail.com", "ASqw1212")

class AddPayment(TestCase):
    def test_add_payment(self):
        addPayment(0, 0, "Visa", "802Academy", "V1V3A4")


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

#here
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


#to verify num of artists - Eric
class ArtistTestCase(TestCase):
    def setUp(self):
        addArtist(1, 'The Electric Tigers', "https://drive.google.com/file/d/1frS-3GGUeoOrFW6Vpk36Aup_1mCnHud1/view?usp=sharing")
        addArtist(2, 'Neon Dreamers', "https://drive.google.com/file/d/1b98JOTnkWdT04ljimUMrSYEUi151gvKU/view?usp=sharing")
        addArtist(3, 'The Funky Monkeys', "https://drive.google.com/file/d/11AxDiz6NpGn4X60yPmuJMe85alfaS-LW/view?usp=sharing")
        addArtist(4, 'Cosmic Groove', "https://drive.google.com/file/d/1CTKRSSXHJYlHia-zKg9T77MC7_L-o9lA/view?usp=sharing")
        addArtist(5, 'Midnight Serenade', "https://drive.google.com/file/d/1ycCM8i6Ub7qQvl-D3Sg27r0LWKQj7H3x/view?usp=sharing")
        addArtist(6, 'Electric Pulse', "https://drive.google.com/file/d/1dLwNNVKN2HQerH-8KyHHK8Il495BG2a7/view?usp=sharing")
        addArtist(7, 'Echo Chamber', "https://drive.google.com/file/d/11ELd3EUYlgwwHbRzjNmTzdVMaesFiQ5D/view?usp=sharing")
        addArtist(8, 'Sonic Boom', "https://drive.google.com/file/d/1fXAKAKYBl-k5P3grS8c2HwcQ0s1d-crA/view?usp=sharing")
        addArtist(9, 'Retro Rockets', "https://drive.google.com/file/d/1AvIqYTozc15UeRJdx3L4308AE41oCPdf/view?usp=sharing")
        addArtist(10, 'The Groove Masters', "https://drive.google.com/file/d/19J9QmNI9ueJXmvDMt-bthiaFODUcFAvx/view?usp=sharing")
        addArtist(11, 'The Funky Jazz Cats', "https://drive.google.com/file/d/1JVrR--lnqNcvCKB4W1k-lbWqPbCRLDn1/view?usp=sharing")
        addArtist(12, 'The Midnight Owls', "https://drive.google.com/file/d/12uw4rZEgGINxIJaK2wzDp148cbv2btf9/view?usp=sharing")
        addArtist(13, 'The Blue Notes', "https://drive.google.com/file/d/1kodm3HbnJKYNqJXBpFf4IKaiQsZaUpQq/view?usp=sharing")
        addArtist(14, 'The Velvet Underground', "https://drive.google.com/file/d/1jwahV58FKmKCkLmsg02sPscoAQhRjDn-/view?usp=sharing")
        addArtist(15, 'The Silk Tones', "https://drive.google.com/file/d/1gqZH8LN4I1V5xAEN4qAteJ9aG12wv19j/view?usp=sharing")
        addArtist(16, 'The Smooth Operators', "https://drive.google.com/file/d/1wOwz1ZL_5kTqdqtLGEdDp9MJjbt3RNCq/view?usp=sharing")
        addArtist(17, 'The Rhythm Rebels', "https://drive.google.com/file/d/1jZH3WCqgTMHBwUf1V1z9RK8G16Ye-Wub/view?usp=sharing")
        addArtist(18, 'The Soul Sisters', "https://drive.google.com/file/d/1pg0y00AW5sTCH9Hq9hdC1KerM9DHF9Y4/view?usp=sharing")
        addArtist(19, 'The Funky Bunch', "https://drive.google.com/file/d/1jw_5t41d6wb_K70Q9aRLRF_YmxMMp8oz/view?usp=sharing")
        addArtist(20, 'The Groovy Gang', "https://drive.google.com/file/d/1jV2iG39xGCS1txJulCuZqkT2rdtn-StM/view?usp=sharing")
        addArtist(21, 'The Jazz Legends', "https://drive.google.com/file/d/1Lb6em21y8FHUw2FpM2n_owJsrLXpccKG/view?usp=sharing")
        addArtist(22, 'The Moonlight Trio', "https://drive.google.com/file/d/1DRkWqyPmQyJsVmc-CgRlVA12zL-FqaMh/view?usp=sharing")
        addArtist(23, 'The Jazz Ensemble', "https://drive.google.com/file/d/1IcqQy_GHo8F0LHMeDztueRv_X7b3yCH1/view?usp=sharing")
        addArtist(24, 'The Harmony Quartet', "https://drive.google.com/file/d/1N9gEICWRnGykhVYBEMBW-jggKUvwf7oq/view?usp=sharing")
        addArtist(25, 'The Jazz Cats', "https://drive.google.com/file/d/10VYlyKRGMD7vUPnmuRdQaepSfOoS2lUk/view?usp=sharing")
        addArtist(26, 'The Swing Set', "https://drive.google.com/file/d/1mMHCeoLNZ3tbS2RjhjMNDANn3pw-O57W/view?usp=sharing")
        addArtist(27, 'The Piano Trio', "https://drive.google.com/file/d/1Yysi95GFCPYh53MuQ7cGgrxtsUzf9Q0-/view?usp=sharing")
        addArtist(28, 'The Funk Masters', "https://drive.google.com/file/d/1mIzzzrsZrVf8yr-OrlLJvvDZQP8uGhbj/view?usp=sharing")
        addArtist(29, 'The Soulful Singers', "https://drive.google.com/file/d/1H5OAwUplsXFGmuJYpiJKHR6tYNxuwskn/view?usp=sharing")
        addArtist(30, 'The Blues Brothers', "https://drive.google.com/file/d/1cYLKevfQ9oSw2_AHpXLlyurguiPBZ7AJ/view?usp=sharing")        
        
        pass

    def test_unique_artists_count(self):
        unique_artists_count = Artists.objects.count()
        expected_count = 30
        self.assertEqual(unique_artists_count, expected_count, "There should be 30 unique artists in the table")

