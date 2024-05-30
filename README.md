# Ticket-Tech

Ticket-Tech is an online ticketing platform that caters to event organizers and attendees. It facilitates the promotion, ticketing, and management of sporting events, concerts, and much more. The platform features tools to create events, customize ticket pricing, manage ticket sales, and handle payments.

## Created By:
- Erem Ozdemir
- Eric Smith
- Ken Anderson
- Nathan Worth
- Kevin Kim

## Description

Ticket-Tech aims to provide a seamless experience for both event organizers and ticket buyers. It includes the following functionalities:

- **Event Creation:** Event organizers can create and customize events.
- **Ticket Management:** Set and manage ticket pricing, availability, and sales.
- **Payment Handling:** Securely process payments and transactions.

## User Groups

### Event Organizers

Event organizers include companies that host events, such as concert promoters, theater productions, and sporting events. Ticket-Tech offers a simple and fast solution for managing events and selling tickets.

**Scenario:** An event organizer uses Ticket-Tech to create an upcoming concert listing. They set ticket pricing, define ticket amounts, and specify venues and cities.

### Ticket Buyers

Ticket buyers are individuals who plan to purchase tickets. They can view trending artists, search for their favorite artists, add tickets to their cart, and make purchases.

**Scenario:** Jack, a fan of the Jazz Legends, uses Ticket-Tech to search for the band, find their venues and cities, add tickets to his cart, and complete the purchase.

### Administrators

Administrators oversee the backend of the platform, managing venues, users, and payments. They also have access to view trends for top artists.

**Scenario:** Eric, an admin, logs into the front end and back end to view data, users, and artists within the system.

## Key Features

- **Search for Artist:** Users can search for artists by name, retrieving all relevant matches.
- **Log In:** Users can log in to access their information.
- **Log Out:** Users can log out of the system.
- **Sign Up:** Users can create an account.
- **Add Concert:** Admins can add concerts to the database, which are then displayed on the front end.
- **Browse Concerts:** Users can browse concerts via a "see more" button.

## Known Bugs

- Shopping cart page does not populate cart items.
- Admin login issues causing automatic front-end login.
- Non-functional "Forgot password" feature.
- User page does not update user information.
- Placeholder payment information.
- Low-quality images due to Google Drive permissions.

## Installation and Setup

To install and run the project:

1. Clone the repository.
2. Install Django following [this guide](https://www.w3schools.com/django/django_install_django.php).
3. Navigate to `Ticket-Tech/Database/mysite`.
4. Set up and activate a virtual environment:
    ```bash
    sudo pip install virtualenv
    virtualenv newenv
    source newenv/bin/activate
    pip install django
    django-admin --version
    ```
5. Run the server:
    ```bash
    python manage.py runserver
    ```

To create a backend user, follow [this guide](https://www.w3schools.com/django/django_admin_create_user.php).

## Project Reflection

Project management was effective, though there were challenges in understanding expectations. Initial requirements were overly ambitious, but the team adapted well, prioritizing essential functionalities and learning new tools. The project provided valuable experience in teamwork, dependency management, and using GitHub for version control and collaboration.

We are proud of what we achieved given our initial knowledge levels and time constraints. It was a valuable learning experience in developing a complex application from scratch.
