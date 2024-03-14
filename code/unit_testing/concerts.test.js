//Ken file
const { fetchConcertData, renderConcerts } = require('./concerts');

test('fetchConcertData returns an array of concerts', async() => {
    const concerts = await fetchConcertData();
    expect(concerts).toHaveLength(3);
    expect(concerts[0]).toHaveProperty('artist');
    expect(concerts[0]).toHaveProperty('venue');
    expect(concerts[0]).toHaveProperty('date');
});

test('renderConcerts renders concerts correctly', () => {
    document.body.innerHTML = '<ul id="concertList"></ul>';
    const concerts = [
        { artist: "Artist 1", venue: "Venue 1", date: "2024-04-01" },
        { artist: "Artist 2", venue: "Venue 2", date: "2024-04-02" },
        { artist: "Artist 3", venue: "Venue 3", date: "2024-04-03" }
    ];
    renderConcerts(concerts);
    const concertList = document.getElementById('concertList');
    expect(concertList.children).toHaveLength(3);
    expect(concertList.children[0].textContent).toContain('Artist 1 - Venue 1, 2024-04-01');
    expect(concertList.children[1].textContent).toContain('Artist 2 - Venue 2, 2024-04-02');
    expect(concertList.children[2].textContent).toContain('Artist 3 - Venue 3, 2024-04-03');
});

// Video on how to do this stuff: https://www.youtube.com/watch?v=x6NUZ8dc9Qg&ab_channel=DaveGray 
// must have Jest downloaded in vscode
// when you run it it will get mad about node, dont worry has nothing to do with us more to do with 
//terminal not having node.js containers