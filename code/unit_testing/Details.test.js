const { fetchConcertInfo, fecthArtistInfo } = require('./Details');

test('Artist name is correct'), async() => {
    const artists = await fecthArtistInfo();
    expect(artists[0].ArtistName == "The Electric Tigers");
}

test('fetchConcertData returns the concert information', async() => {
    const concerts = await fetchConcertInfo();
    expect(concerts[0]).toHaveProperty('ConcertId');
    expect(concerts[0]).toHaveProperty('ArtistId');
    expect(concerts[0]).toHaveProperty('ConcertDate');
    expect(concerts[0]).toHaveProperty('Venue');
    expect(concerts[0]).toHaveProperty('City');
    expect(concerts[0]).toHaveProperty('TicketPrice');
    expect(concerts[0]).toHaveProperty('Ticketquantity');
});