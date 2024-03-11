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

testDisplay()