
from django.test import TestCase
from django.shortcuts import render, HttpResponse
from .views import addConcert
from .views import addArtist
from .views import addClient
from .views import addPayment
from .views import addMyTickets
from .views import addCart

from .models import Artists
from .models import Concerts
from .models import client
from .models import payment
from .models import myTickets
from .views import removeArtist
from .views import removeConcert
from .models import Artists
from .models import Concerts
from .models import cart


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

class AddCart(TestCase):
    def test_add_cart(self):
        addCart(0,0)

        cart2 = cart.object.get(userId = 0)
        self.assertEqual(cart2.userId, 0)

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
class ArtistNumTestCase(TestCase):
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



class ConcertNumTestCase(TestCase):
    def setUp(self):
        addConcert(1, 1, '2024-03-05', 'Electric Plaza', 'Uptown', 500, 85.00)
        addConcert(2, 1, '2024-03-15', 'Neon Arena', 'Downtown', 1000, 90.00)
        addConcert(3, 1, '2024-04-01', 'Rock Dome', 'Metropolis', 1500, 95.00)
        addConcert(4, 1, '2024-04-15', 'Harmony Hall', 'Harmony', 800, 100.00)
        addConcert(5, 1, '2024-05-02', 'Sunset Pavilion', 'Riverside', 1200, 105.00)
        addConcert(6, 2, '2024-03-10', 'Sunset Garden', 'Riverside', 700, 90.00)
        addConcert(7, 2, '2024-03-20', 'Indie Hall', 'Uptown', 900, 95.00)
        addConcert(8, 2, '2024-04-05', 'Jazz Plaza', 'Downtown', 1100, 100.00)
        addConcert(9, 2, '2024-04-18', 'Lakeside Arena', 'Lakeside', 600, 105.00)
        addConcert(10, 2, '2024-05-05', 'Metro Hall', 'Metropolis', 1000, 110.00)
        addConcert(11, 3, '2024-03-15', 'Jazz Lounge', 'Riverside', 800, 95.00)
        addConcert(12, 3, '2024-03-30', 'Funky Arena', 'Downtown', 1200, 100.00)
        addConcert(13, 3, '2024-04-10', 'Groove Plaza', 'Uptown', 1000, 105.00)
        addConcert(14, 3, '2024-04-22', 'Central Stadium', 'Central', 2000, 110.00)
        addConcert(15, 3, '2024-05-07', 'Sunset Garden', 'Harmony', 600, 115.00)
        addConcert(16, 4, '2024-03-20', 'Central Stadium', 'Central', 2000, 110.00)
        addConcert(17, 4, '2024-04-05', 'Jazz Lounge', 'Riverside', 800, 115.00)
        addConcert(18, 4, '2024-04-15', 'Groove Plaza', 'Uptown', 1000, 120.00)
        addConcert(19, 4, '2024-04-27', 'Rock Arena', 'Metropolis', 1500, 125.00)
        addConcert(20, 4, '2024-05-12', 'Electric Garden', 'West End', 300, 130.00)
        addConcert(21, 5, '2024-03-25', 'Riverfront Amphitheater', 'Lakeside', 4000, 120.00)
        addConcert(22, 5, '2024-04-10', 'Sunset Lounge', 'Harmony', 800, 125.00)
        addConcert(23, 5, '2024-04-20', 'City Stadium', 'Central', 2000, 130.00)
        addConcert(24, 5, '2024-05-05', 'Indie Hall', 'Uptown', 900, 135.00)
        addConcert(25, 5, '2024-05-18', 'Metro Plaza', 'Metropolis', 1000, 140.00)
        addConcert(26, 6, '2024-03-30', 'Electric Arena', 'Uptown', 900, 125.00)
        addConcert(27, 6, '2024-04-10', 'Pulse Pavilion', 'Harmony', 800, 130.00)
        addConcert(28, 6, '2024-04-25', 'Echo Lounge', 'Metropolis', 1000, 135.00)
        addConcert(29, 6, '2024-05-08', 'Sonic Stadium', 'Eastside', 700, 140.00)
        addConcert(30, 6, '2024-05-22', 'Electric Plaza', 'Uptown', 500, 145.00)
        addConcert(31, 7, '2024-03-04', 'Echo Hall', 'Metropolis', 1500, 130.00)
        addConcert(32, 7, '2024-03-20', 'Echo Lounge', 'Metropolis', 1000, 135.00)
        addConcert(33, 7, '2024-04-10', 'Echo Stadium', 'Metropolis', 2000, 140.00)
        addConcert(34, 7, '2024-04-20', 'Echo Plaza', 'Metropolis', 1200, 145.00)
        addConcert(35, 7, '2024-05-10', 'Echo Garden', 'Metropolis', 800, 150.00)
        addConcert(36, 8, '2024-03-05', 'Sonic Stadium', 'Eastside', 700, 135.00)
        addConcert(37, 8, '2024-03-15', 'Sonic Hall', 'Eastside', 900, 140.00)
        addConcert(38, 8, '2024-04-01', 'Sonic Plaza', 'Eastside', 1100, 145.00)
        addConcert(39, 8, '2024-04-15', 'Sonic Garden', 'Eastside', 600, 150.00)
        addConcert(40, 8, '2024-05-02', 'Sonic Arena', 'Eastside', 1000, 155.00)
        addConcert(41, 9, '2024-03-08', 'Retro Plaza', 'West End', 1000, 140.00)
        addConcert(42, 9, '2024-03-20', 'Retro Lounge', 'West End', 1200, 145.00)
        addConcert(43, 9, '2024-04-05', 'Retro Garden', 'West End', 600, 150.00)
        addConcert(44, 9, '2024-04-15', 'Retro Stadium', 'West End', 2000, 155.00)
        addConcert(45, 9, '2024-05-01', 'Retro Arena', 'West End', 900, 160.00)
        addConcert(46, 10, '2024-03-02', 'Groove Arena', 'Central', 2000, 145.00)
        addConcert(47, 10, '2024-03-15', 'Groove Lounge', 'Central', 1200, 150.00)
        addConcert(48, 10, '2024-04-01', 'Groove Plaza', 'Central', 1500, 155.00)
        addConcert(49, 10, '2024-04-18', 'Groove Garden', 'Central', 700, 160.00)
        addConcert(50, 10, '2024-05-05', 'Groove Hall', 'Central', 1000, 165.00)
        addConcert(51, 11, '2024-03-07', 'Jazz Plaza', 'Riverside', 1000, 150.00)
        addConcert(52, 11, '2024-03-16', 'Jazz Lounge', 'Riverside', 1200, 155.00)
        addConcert(53, 11, '2024-04-01', 'Jazz Plaza', 'Riverside', 900, 160.00)
        addConcert(54, 11, '2024-04-18', 'Jazz Stadium', 'Riverside', 800, 165.00)
        addConcert(55, 11, '2024-05-01', 'Jazz Garden', 'Riverside', 1100, 170.00)
        addConcert(56, 12, '2024-03-07', 'Owl''s Nest', 'Lakeside', 800, 155.00)
        addConcert(57, 12, '2024-03-16', 'Midnight Lounge', 'Lakeside', 1000, 160.00)
        addConcert(58, 12, '2024-04-01', 'Midnight Plaza', 'Lakeside', 1200, 165.00)
        addConcert(59, 13, '2024-03-10', 'Blue Lounge', 'Uptown', 800, 160.00)
        addConcert(60, 13, '2024-03-20', 'Blue Plaza', 'Uptown', 1000, 165.00)
        addConcert(61, 13, '2024-04-05', 'Blue Garden', 'Uptown', 1200, 170.00)
        addConcert(62, 13, '2024-04-18', 'Blue Stadium', 'Uptown', 900, 175.00)
        addConcert(63, 13, '2024-05-01', 'Blue Arena', 'Uptown', 1100, 180.00)
        addConcert(64, 14, '2024-03-08', 'Velvet Lounge', 'Downtown', 900, 165.00)
        addConcert(65, 14, '2024-03-18', 'Velvet Plaza', 'Downtown', 1100, 170.00)

        pass
    
    def test_unique_concerts_count(self):
        unique_concerts_count = Concerts.objects.count()
        expected_concerts = 65
        self.assertEqual(unique_concerts_count, expected_concerts, "There should be 65 unique concerts")