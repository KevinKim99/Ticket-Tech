-- Create Artists table
CREATE TABLE Artists (
    ArtistId INTEGER PRIMARY KEY,
    ArtistName VARCHAR(255),
    ArtistImage VARCHAR(255)
);

-- Create Concerts table
CREATE TABLE Concerts (
    ConcertId INTEGER PRIMARY KEY,
    ArtistId INTEGER,
    ConcertDate DATETIME,
    Venue VARCHAR(255),
    City VARCHAR(255),
    TicketQuantity INTEGER,
    TicketPrice DOUBLE(4,2),
    FOREIGN KEY (ArtistId) REFERENCES Artists(ArtistId)
);


-- Insert data into Artists table
INSERT INTO Artists (ArtistId, ArtistName, ArtistImage)
VALUES
    (1, 'The Electric Tigers', "https://drive.google.com/file/d/1frS-3GGUeoOrFW6Vpk36Aup_1mCnHud1/view?usp=sharing"),
    (2, 'Neon Dreamers', "https://drive.google.com/file/d/1b98JOTnkWdT04ljimUMrSYEUi151gvKU/view?usp=sharing"),
    (3, 'The Funky Monkeys', "https://drive.google.com/file/d/11AxDiz6NpGn4X60yPmuJMe85alfaS-LW/view?usp=sharing"),
    (4, 'Cosmic Groove', "https://drive.google.com/file/d/1CTKRSSXHJYlHia-zKg9T77MC7_L-o9lA/view?usp=sharing"),
    (5, 'Midnight Serenade', "https://drive.google.com/file/d/1ycCM8i6Ub7qQvl-D3Sg27r0LWKQj7H3x/view?usp=sharing"),
    (6, 'Electric Pulse', "https://drive.google.com/file/d/1dLwNNVKN2HQerH-8KyHHK8Il495BG2a7/view?usp=sharing"),
    (7, 'Echo Chamber', "https://drive.google.com/file/d/11ELd3EUYlgwwHbRzjNmTzdVMaesFiQ5D/view?usp=sharing"),
    (8, 'Sonic Boom', "https://drive.google.com/file/d/1fXAKAKYBl-k5P3grS8c2HwcQ0s1d-crA/view?usp=sharing"),
    (9, 'Retro Rockets', "https://drive.google.com/file/d/1AvIqYTozc15UeRJdx3L4308AE41oCPdf/view?usp=sharing"),
    (10, 'The Groove Masters', "https://drive.google.com/file/d/19J9QmNI9ueJXmvDMt-bthiaFODUcFAvx/view?usp=sharing"),
    (11, 'The Funky Jazz Cats', "https://drive.google.com/file/d/1JVrR--lnqNcvCKB4W1k-lbWqPbCRLDn1/view?usp=sharing"),
    (12, 'The Midnight Owls', "https://drive.google.com/file/d/12uw4rZEgGINxIJaK2wzDp148cbv2btf9/view?usp=sharing"),
    (13, 'The Blue Notes', "https://drive.google.com/file/d/1kodm3HbnJKYNqJXBpFf4IKaiQsZaUpQq/view?usp=sharing"),
    (14, 'The Velvet Underground', "https://drive.google.com/file/d/1jwahV58FKmKCkLmsg02sPscoAQhRjDn-/view?usp=sharing"),
    (15, 'The Silk Tones', "https://drive.google.com/file/d/1gqZH8LN4I1V5xAEN4qAteJ9aG12wv19j/view?usp=sharing"),
    (16, 'The Smooth Operators', "https://drive.google.com/file/d/1wOwz1ZL_5kTqdqtLGEdDp9MJjbt3RNCq/view?usp=sharing"),
    (17, 'The Rhythm Rebels', "https://drive.google.com/file/d/1jZH3WCqgTMHBwUf1V1z9RK8G16Ye-Wub/view?usp=sharing"),
    (18, 'The Soul Sisters', "https://drive.google.com/file/d/1pg0y00AW5sTCH9Hq9hdC1KerM9DHF9Y4/view?usp=sharing"),
    (19, 'The Funky Bunch', "https://drive.google.com/file/d/1jw_5t41d6wb_K70Q9aRLRF_YmxMMp8oz/view?usp=sharing"),
    (20, 'The Groovy Gang', "https://drive.google.com/file/d/1jV2iG39xGCS1txJulCuZqkT2rdtn-StM/view?usp=sharing"),
    (21, 'The Jazz Legends', "https://drive.google.com/file/d/1Lb6em21y8FHUw2FpM2n_owJsrLXpccKG/view?usp=sharing"),
    (22, 'The Moonlight Trio', "https://drive.google.com/file/d/1DRkWqyPmQyJsVmc-CgRlVA12zL-FqaMh/view?usp=sharing"),
    (23, 'The Jazz Ensemble', "https://drive.google.com/file/d/1IcqQy_GHo8F0LHMeDztueRv_X7b3yCH1/view?usp=sharing"),
    (24, 'The Harmony Quartet', "https://drive.google.com/file/d/1N9gEICWRnGykhVYBEMBW-jggKUvwf7oq/view?usp=sharing"),
    (25, 'The Jazz Cats', "https://drive.google.com/file/d/10VYlyKRGMD7vUPnmuRdQaepSfOoS2lUk/view?usp=sharing"),
    (26, 'The Swing Set', "https://drive.google.com/file/d/1mMHCeoLNZ3tbS2RjhjMNDANn3pw-O57W/view?usp=sharing"),
    (27, 'The Piano Trio', "https://drive.google.com/file/d/1Yysi95GFCPYh53MuQ7cGgrxtsUzf9Q0-/view?usp=sharing"),
    (28, 'The Funk Masters', "https://drive.google.com/file/d/1mIzzzrsZrVf8yr-OrlLJvvDZQP8uGhbj/view?usp=sharing"),
    (29, 'The Soulful Singers', "https://drive.google.com/file/d/1H5OAwUplsXFGmuJYpiJKHR6tYNxuwskn/view?usp=sharing"),
    (30, 'The Blues Brothers', "https://drive.google.com/file/d/1cYLKevfQ9oSw2_AHpXLlyurguiPBZ7AJ/view?usp=sharing");

-- Insert data into Concerts table
INSERT INTO Concerts (ArtistId, ConcertDate, Venue, City, TicketQuantity, TicketPrice)
VALUES
    (1, '2024-03-05', 'Electric Plaza', 'Uptown', 500, 85.00),
    (1, '2024-03-15', 'Neon Arena', 'Downtown', 1000, 90.00),
    (1, '2024-04-01', 'Rock Dome', 'Metropolis', 1500, 95.00),
    (1, '2024-04-15', 'Harmony Hall', 'Harmony', 800, 100.00),
    (1, '2024-05-02', 'Sunset Pavilion', 'Riverside', 1200, 105.00),
    (2, '2024-03-10', 'Sunset Garden', 'Riverside', 700, 90.00),
    (2, '2024-03-20', 'Indie Hall', 'Uptown', 900, 95.00),
    (2, '2024-04-05', 'Jazz Plaza', 'Downtown', 1100, 100.00),
    (2, '2024-04-18', 'Lakeside Arena', 'Lakeside', 600, 105.00),
    (2, '2024-05-05', 'Metro Hall', 'Metropolis', 1000, 110.00),
    (3, '2024-03-15', 'Jazz Lounge', 'Riverside', 800, 95.00),
    (3, '2024-03-30', 'Funky Arena', 'Downtown', 1200, 100.00),
    (3, '2024-04-10', 'Groove Plaza', 'Uptown', 1000, 105.00),
    (3, '2024-04-22', 'Central Stadium', 'Central', 2000, 110.00),
    (3, '2024-05-07', 'Sunset Garden', 'Harmony', 600, 115.00),
    (4, '2024-03-20', 'Central Stadium', 'Central', 2000, 110.00),
    (4, '2024-04-05', 'Jazz Lounge', 'Riverside', 800, 115.00),
    (4, '2024-04-15', 'Groove Plaza', 'Uptown', 1000, 120.00),
    (4, '2024-04-27', 'Rock Arena', 'Metropolis', 1500, 125.00),
    (4, '2024-05-12', 'Electric Garden', 'West End', 300, 130.00),
    (5, '2024-03-25', 'Riverfront Amphitheater', 'Lakeside', 4000, 120.00),
    (5, '2024-04-10', 'Sunset Lounge', 'Harmony', 800, 125.00),
    (5, '2024-04-20', 'City Stadium', 'Central', 2000, 130.00),
    (5, '2024-05-05', 'Indie Hall', 'Uptown', 900, 135.00),
    (5, '2024-05-18', 'Metro Plaza', 'Metropolis', 1000, 140.00),
    (6, '2024-03-30', 'Electric Arena', 'Uptown', 900, 125.00),
    (6, '2024-04-10', 'Pulse Pavilion', 'Harmony', 800, 130.00),
    (6, '2024-04-25', 'Echo Lounge', 'Metropolis', 1000, 135.00),
    (6, '2024-05-08', 'Sonic Stadium', 'Eastside', 700, 140.00),
    (6, '2024-05-22', 'Electric Plaza', 'Uptown', 500, 145.00),
    (7, '2024-03-04', 'Echo Hall', 'Metropolis', 1500, 130.00),
    (7, '2024-03-20', 'Echo Lounge', 'Metropolis', 1000, 135.00),
    (7, '2024-04-10', 'Echo Stadium', 'Metropolis', 2000, 140.00),
    (7, '2024-04-20', 'Echo Plaza', 'Metropolis', 1200, 145.00),
    (7, '2024-05-10', 'Echo Garden', 'Metropolis', 800, 150.00),
    (8, '2024-03-05', 'Sonic Stadium', 'Eastside', 700, 135.00),
    (8, '2024-03-15', 'Sonic Hall', 'Eastside', 900, 140.00),
    (8, '2024-04-01', 'Sonic Plaza', 'Eastside', 1100, 145.00),
    (8, '2024-04-15', 'Sonic Garden', 'Eastside', 600, 150.00),
    (8, '2024-05-02', 'Sonic Arena', 'Eastside', 1000, 155.00),
    (9, '2024-03-08', 'Retro Plaza', 'West End', 1000, 140.00),
    (9, '2024-03-20', 'Retro Lounge', 'West End', 1200, 145.00),
    (9, '2024-04-05', 'Retro Garden', 'West End', 600, 150.00),
    (9, '2024-04-15', 'Retro Stadium', 'West End', 2000, 155.00),
    (9, '2024-05-01', 'Retro Arena', 'West End', 900, 160.00),
    (10, '2024-03-02', 'Groove Arena', 'Central', 2000, 145.00),
    (10, '2024-03-15', 'Groove Lounge', 'Central', 1200, 150.00),
    (10, '2024-04-01', 'Groove Plaza', 'Central', 1500, 155.00),
    (10, '2024-04-18', 'Groove Garden', 'Central', 700, 160.00),
    (10, '2024-05-05', 'Groove Hall', 'Central', 1000, 165.00),
    (11, '2024-03-07', 'Jazz Plaza', 'Riverside', 1000, 150.00),
    (11, '2024-03-16', 'Jazz Lounge', 'Riverside', 1200, 155.00),
    (11, '2024-04-01', 'Jazz Plaza', 'Riverside', 900, 160.00),
    (11, '2024-04-18', 'Jazz Stadium', 'Riverside', 800, 165.00),
    (11, '2024-05-01', 'Jazz Garden', 'Riverside', 1100, 170.00),
    (12, '2024-03-07', 'Owl''s Nest', 'Lakeside', 800, 155.00),
    (12, '2024-03-16', 'Midnight Lounge', 'Lakeside', 1000, 160.00),
    (12, '2024-04-01', 'Midnight Plaza', 'Lakeside', 1200, 165.00),
    (13, '2024-03-10', 'Blue Lounge', 'Uptown', 800, 160.00),
    (13, '2024-03-20', 'Blue Plaza', 'Uptown', 1000, 165.00),
    (13, '2024-04-05', 'Blue Garden', 'Uptown', 1200, 170.00),
    (13, '2024-04-18', 'Blue Stadium', 'Uptown', 900, 175.00),
    (13, '2024-05-01', 'Blue Arena', 'Uptown', 1100, 180.00),
    (14, '2024-03-08', 'Velvet Lounge', 'Downtown', 900, 165.00),
    (14, '2024-03-18', 'Velvet Plaza', 'Downtown', 1100, 170.00),
    (14, '2024-04-02', 'Velvet Garden', 'Downtown', 1300, 175.00),
    (14, '2024-04-15', 'Velvet Stadium', 'Downtown', 1000, 180.00),
    (14, '2024-05-02', 'Velvet Arena', 'Downtown', 1200, 185.00),
    (15, '2024-03-05', 'Silk Lounge', 'Metropolis', 1000, 170.00),
    (15, '2024-03-15', 'Silk Plaza', 'Metropolis', 1200, 175.00),
    (15, '2024-04-01', 'Silk Garden', 'Metropolis', 1400, 180.00),
    (15, '2024-04-18', 'Silk Stadium', 'Metropolis', 1100, 185.00),
    (15, '2024-05-05', 'Silk Arena', 'Metropolis', 1300, 190.00),
    (16, '2024-03-10', 'Smooth Lounge', 'Harmony', 1100, 175.00),
    (16, '2024-03-20', 'Smooth Plaza', 'Harmony', 1300, 180.00),
    (16, '2024-04-05', 'Smooth Garden', 'Harmony', 1500, 185.00),
    (16, '2024-04-18', 'Smooth Stadium', 'Harmony', 1200, 190.00),
    (16, '2024-05-01', 'Smooth Arena', 'Harmony', 1400, 195.00),
    (17, '2024-03-15', 'Rebel Lounge', 'Lakeside', 1200, 180.00),
    (17, '2024-03-30', 'Rebel Plaza', 'Lakeside', 1400, 185.00),
    (17, '2024-04-10', 'Rebel Garden', 'Lakeside', 1600, 190.00),
    (17, '2024-04-22', 'Rebel Stadium', 'Lakeside', 1300, 195.00),
    (17, '2024-05-07', 'Rebel Arena', 'Lakeside', 1500, 200.00),
    (18, '2024-03-20', 'Soul Lounge', 'West End', 1300, 185.00),
    (18, '2024-04-05', 'Soul Plaza', 'West End', 1500, 190.00),
    (18, '2024-04-15', 'Soul Garden', 'West End', 1700, 195.00),
    (18, '2024-04-27', 'Soul Stadium', 'West End', 1400, 200.00),
    (18, '2024-05-12', 'Soul Arena', 'West End', 1600, 205.00),
    (19, '2024-03-25', 'Funky Lounge', 'Central', 1400, 190.00),
    (19, '2024-04-10', 'Funky Plaza', 'Central', 1600, 195.00),
    (19, '2024-04-20', 'Funky Garden', 'Central', 1800, 200.00),
    (19, '2024-05-05', 'Funky Stadium', 'Central', 1500, 205.00),
    (19, '2024-05-18', 'Funky Arena', 'Central', 1700, 210.00),
    (20, '2024-03-30', 'Groovy Lounge', 'Riverside', 1500, 195.00),
    (20, '2024-04-10', 'Groovy Plaza', 'Riverside', 1700, 200.00),
    (20, '2024-04-25', 'Groovy Garden', 'Riverside', 1900, 205.00),
    (20, '2024-05-08', 'Groovy Stadium', 'Riverside', 1600, 210.00),
    (20, '2024-05-22', 'Groovy Arena', 'Riverside', 1800, 215.00),
    (21, '2024-03-04', 'Jazz Lounge', 'Uptown', 900, 195.00),
    (21, '2024-03-20', 'Jazz Plaza', 'Uptown', 1100, 200.00),
    (21, '2024-04-10', 'Jazz Garden', 'Uptown', 1300, 205.00),
    (21, '2024-04-20', 'Jazz Stadium', 'Uptown', 1000, 210.00),
    (21, '2024-05-10', 'Jazz Arena', 'Uptown', 1200, 215.00),
    (22, '2024-03-05', 'Moonlight Lounge', 'Downtown', 1000, 200.00),
    (22, '2024-03-15', 'Moonlight Plaza', 'Downtown', 1200, 205.00),
    (22, '2024-04-01', 'Moonlight Garden', 'Downtown', 1400, 210.00),
    (22, '2024-04-18', 'Moonlight Stadium', 'Downtown', 1100, 215.00),
    (22, '2024-05-02', 'Moonlight Arena', 'Downtown', 1300, 220.00),
    (23, '2024-03-10', 'Jazz Lounge', 'Metropolis', 1100, 205.00),
    (23, '2024-03-20', 'Jazz Plaza', 'Metropolis', 1300, 210.00),
    (23, '2024-04-05', 'Jazz Garden', 'Metropolis', 1500, 215.00),
    (23, '2024-04-18', 'Jazz Stadium', 'Metropolis', 1200, 220.00),
    (23, '2024-05-01', 'Jazz Arena', 'Metropolis', 1400, 225.00),
    (24, '2024-03-15', 'Harmony Lounge', 'Harmony', 1200, 210.00),
    (24, '2024-03-30', 'Harmony Plaza', 'Harmony', 1400, 215.00),
    (24, '2024-04-10', 'Harmony Garden', 'Harmony', 1600, 220.00),
    (24, '2024-04-22', 'Harmony Stadium', 'Harmony', 1300, 225.00),
    (24, '2024-05-07', 'Harmony Arena', 'Harmony', 1500, 230.00),
    (25, '2024-03-20', 'Jazz Lounge', 'Lakeside', 1300, 215.00),
    (25, '2024-04-05', 'Jazz Plaza', 'Lakeside', 1500, 220.00),
    (25, '2024-04-15', 'Jazz Garden', 'Lakeside', 1700, 225.00),
    (25, '2024-04-27', 'Jazz Stadium', 'Lakeside', 1400, 230.00),
    (25, '2024-05-12', 'Jazz Arena', 'Lakeside', 1600, 235.00),
    (26, '2024-03-25', 'Swing Lounge', 'West End', 1400, 220.00),
    (26, '2024-04-10', 'Swing Plaza', 'West End', 1600, 225.00),
    (26, '2024-04-20', 'Swing Garden', 'West End', 1800, 230.00),
    (26, '2024-05-05', 'Swing Stadium', 'West End', 1500, 235.00),
    (26, '2024-05-18', 'Swing Arena', 'West End', 1700, 240.00),
    (27, '2024-03-30', 'Piano Lounge', 'Central', 1500, 225.00),
    (27, '2024-04-10', 'Piano Plaza', 'Central', 1700, 230.00),
    (27, '2024-04-25', 'Piano Garden', 'Central', 1900, 235.00),
    (27, '2024-05-08', 'Piano Stadium', 'Central', 1600, 240.00),
    (27, '2024-05-22', 'Piano Arena', 'Central', 1800, 245.00),
    (28, '2024-03-04', 'Funk Lounge', 'Riverside', 900, 225.00),
    (28, '2024-03-20', 'Funk Plaza', 'Riverside', 1100, 230.00),
    (28, '2024-04-10', 'Funk Garden', 'Riverside', 1300, 235.00),
    (28, '2024-04-20', 'Funk Stadium', 'Riverside', 1000, 240.00),
    (28, '2024-05-10', 'Funk Arena', 'Riverside', 1200, 245.00),
    (29, '2024-03-08', 'Soulful Lounge', 'Uptown', 900, 230.00),
    (29, '2024-03-18', 'Soulful Plaza', 'Uptown', 1100, 235.00),
    (29, '2024-04-02', 'Soulful Garden', 'Uptown', 1300, 240.00),
    (29, '2024-04-15', 'Soulful Stadium', 'Uptown', 1000, 245.00),
    (29, '2024-05-02', 'Soulful Arena', 'Uptown', 1200, 250.00),
    (30, '2024-05-05', 'Blues Arena', 'Downtown', 1100, 250.00);
