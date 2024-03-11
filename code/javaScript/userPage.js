let tab = 0;

const ticket = document.getElementById("ticket");
const profile = document.getElementById("profile");
const payment = document.getElementById("payment");

const ticketBtn = document.getElementById("ticketButton");
const profileBtn = document.getElementById("profileButton");
const paymentBtn = document.getElementById("paymentButton");



ticketBtn.addEventListener("click", (event) => {
    
    profile.classList.add("noneDisplay")
    payment.classList.add("noneDisplay")
    if (ticket.classList.contains("noneDisplay")){
        ticket.classList.remove("noneDisplay");
    }
});

profileBtn.addEventListener("click", (event) => {

    ticket.classList.add("noneDisplay")
    payment.classList.add("noneDisplay")
    if (profile.classList.contains("noneDisplay")){
        profile.classList.remove("noneDisplay");
    }

});

paymentBtn.addEventListener("click", (event) => {

    ticket.classList.add("noneDisplay")
    profile.classList.add("noneDisplay")
    if (payment.classList.contains("noneDisplay")){
        payment.classList.remove("noneDisplay");
    }

});