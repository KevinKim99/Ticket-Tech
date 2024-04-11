let tab = 0;

const ticket = document.getElementById("ticket");
const profile = document.getElementById("profile");
const payment = document.getElementById("payment");

const ticketBtn = document.getElementById("ticketButton");
const profileBtn = document.getElementById("profileButton");
const paymentBtn = document.getElementById("paymentButton");

const userNameInput = document.getElementById("profileName");
const emailInput = document.getElementById("profileEmail")
const passwordInput = document.getElementById("profilePassword")

const updateBtn = document.getElementById("btn");

updateBtn.addEventListener("click", function(event) {
    console.log('Btn clicekd');
    const userName = document.getElementById("profileName").value;
    const userEmail = document.getElementById('profileEmail').value;
    const userPassword = document.getElementById('profilePassword').value;

    updateUserProfile(userName, userEmail, userPassword);
})
    
function updateUserProfile(userName, userEmail, userPassword){
    fetch('update_profile/', {
        method: 'POST',
        body: JSON.stringify({
            userName: userName,
            userEmail: userEmail,
            userPassword: userPassword
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('Profile updated: ', data);
        alert("Profile updated successfully");
    })
    .catch(error => {
        console.error("Error during update: ", error);
        alert("Error updaing profile: " + error.message);
    });

}

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

