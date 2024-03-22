const { fetchConcertData } = require('./code/Details.html');

test('Artist name is correct'), async() => {
    const concerts = await fetchConcertData();
    expect(concerts[0] == "Artist1");
}

test('fetchConcertData returns the concert information', async() => {
    const concerts = await fetchConcertData();
    expect(concerts).toHaveLength(1);
    expect(concerts[0]).toHaveProperty('artist');
    expect(concerts[0]).toHaveProperty('venue');
    expect(concerts[0]).toHaveProperty('date');
    expect(concerts[0]).toHaveProperty('price');
    expect(concerts[0]).toHaveProperty('quantity');
});