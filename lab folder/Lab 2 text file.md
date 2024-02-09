# Lab 2 txt file

![lab2_usercase](/images/lab_2_user_cases.png)

## Use Case 1 - Search for Venue

**Primary actor:** Users (purchasers)

**Scope:** Concert fans / sports fans

**Level:** User goal

**Stakeholders and interests:**

**Purchaser:** wants to browse venues and find one near them.

**Admin:** wants to observe who is browsing certain venues?

**Precondition:** User must access Ticket-Tech, search function must work.

**Minimal Guarantee:** Venue or group of venues is selected and allows user to see upcoming events at venue

**Success Guarantee:** Venue or group of venues is selected and events at venues are recommended to users. 

**Main success scenario:**

User wants to purchase a ticket for a certain event
User searches for a venue or an area
Ticket-Tech shows the venue or venues in the given area
User gets access to venue and can see all upcoming events and dates at a certain venue
User can choose events they want to purchase tickets for

**Extensions:**
2a. Venue not found in location
	2a1 display simple error message stating no results found


## Use Case 2 - log in

**Primary actor:** Users

**Scope:** Concert fans / sports fans

**Level:** User goal

**Stakeholders and interests:**

User wants to sign into their account
Ticket-Tech wants to store info about a user
Precondition: User has account and has selected a venue to purchase a ticket for

**Minimal guarantee:** user is able to sign in

**Success guarantee:** user is able to sign in and account information is loaded correctly. Future recommendations are given based on user preferences.

**Main Success Scenario:**

If user has an account, sign in and stay signed in while browsing venues / events
Store user info eg phone number, email, location, previous orders
User is logged in and is able to purchase tickets
Information for recommendations is collected during browsing time.

**Extensions:**
2a. Wrong password entered
	2a1 simple error message stating wrong password


## Use Case 3 - Promotional / Sales / Presales

**Primary actor:** Admin
**Scope:** Ticket-Tech promotional department
**Level:** Admin goal

**Stakeholders and interests:**

**Purchaser:** who wants to buy the promotion deal on certain tickets 

**Precondition:** User already has an account in the platform

**Minimal Guarantee:** User is able to purchase tickets on sale.

**Success Guarantee:** User bought the ticket with a promotional deal, updates user transaction with the discounted price they bought at 

**Main success scenario:**

User logs into the platform and 
Finds the promotional section on the top
Clicks into it
Sees what the tickets are on discount
They can also find certain tickets by searching function
Proceeds the to purchase with discounted price
Shows the updated discounted price on users transaction

**Extensions:**
2a. Venue not found in location
	2a1 display simple error message stating no results found
3a. Tickets sold in between selection and checkout
	3a1 display error message stating tickets are already sold



