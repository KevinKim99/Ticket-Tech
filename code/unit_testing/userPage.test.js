function setUpTestingEnvironment() {
    ticket.classList.add("noneDisplay");
    profile.classList.add("noneDisplay");
    payment.classList.add("noneDisplay");
}

function testDisplay() {
    setUpTestingEnvironment();
    
    ticketBtn.click();
    if(!ticket.classList.contains("noneDisplay") && profile.classList.contains("noneDisplay") && payment.classList.contains("noneDisplay")){
        console.log("Success: My Tickets tab is displayed correctly.");
    } else {
        console.error("Error: My Ticketstab display is incorrect.");
    }

    profileBtn.click();
    if(ticket.classList.contains("noneDisplay") && !profile.classList.contains("noneDisplay") && payment.classList.contains("noneDisplay")){
        console.log("Success: Profile Information tab is displayed correctly.");
    } else {
        console.error("Error: Profile Information tab display is incorrect.");
    }

    paymentBtn.click();
    if(ticket.classList.contains("noneDisplay") && profile.classList.contains("noneDisplay") && !payment.classList.contains("noneDisplay")){
        console.log("Success: Payment Information tab is displayed correctly.");
    } else {
        console.error("Error: Payment Information tab display is incorrect.");
    }
}

const { fetchClientData } = require('./code/userPage.html');

test('Testing user name is correct'), async() => {
    const client = await fetchClientData();
    expect(client[0] == "tester")
}

test('fetchClientData returns client information', async() => {
    const client = await fetchClientData();
    expect(client[0]).toHaveProperty('tester');
    expect(client[0]).toHaveProperty('tester@gmail.com');
    expect(client[0]).toHaveProperty('testerpassword');
})



testDisplay()