// Define a global variable to store the cart items
let cartItems = [];

// Function to add an item to the cart
function addToCart(artist, price) {
    const item = { artist, price };
    cartItems.push(item);
    updateCartIcon();
}

// Function to show the cart
function showCart() {
    if (cartItems.length > 0) {
        alert("Cart Items:\n" + cartItems.map(item => `${item.artist} - $${item.price}`).join('\n'));
    } else {
        alert("Your cart is empty.");
    }
}

// Function to update the cart icon
function updateCartIcon() {
    const cartIcon = document.getElementById('cart-icon');
    if (cartItems.length > 0) {
        // if items in cart then color of cart will be red
        cartIcon.style.color = 'red';
    } else {
        // Reset the color or badge
        cartIcon.style.color = 'black';
    }

    // event listener for cart click function
    cartIcon.addEventListener('click', function() {
        window.location.href = 'cart.html';
    });
}

// display cart items method.
function displayCartContent() {
    const cartContentContainer = document.getElementById('cartContent');
    if (cartItems.length > 0) {
        const cartHTML = cartItems.map(item => `<p>${item.artist} - $${item.price}</p>`).join('');
        cartContentContainer.innerHTML = `<h2>Your Cart</h2>${cartHTML}`;
    } else {
        // If cart is empty,call error method
        displayCartError();
    }
}

// Function to display an error message when the cart is empty only works in web browser
function displayCartError() {
    const cartContentContainer = document.getElementById('cartContent');
    cartContentContainer.innerHTML = '<p>Your cart is empty. Add items to continue.</p>';
}