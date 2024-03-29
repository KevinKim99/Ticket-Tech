# M2: Project Description and Requirements
## DUE Feb 16, 11:59pm

### For this milestone, you need to submit a pdf report with the following details of your project:

- What your project is
    - Ticket Tech is an online ticket selling platform, it allows users to be able to buy, sell and resell tickest for sports events, concerts and much more for their favorite artists. Ticket Tech aims to create a seamless experience for the user to be able to purchase tickets. 
- A high-level description of what your project will offer. The description needs to adequately detail a summary of what it will do, but you have a lot of freedom to decide what your final product will look like as long as you perform a realistic analysis of the problem.  
    - Ticket Tech aims to offer a streamlined app that allows users to purchase tickets for their favorite artists. Ticket Tech will allow users to keep track of events going on nearby, keep track of their favorite artists and track what events and locations they are apart of. Key Features of Ticket Tech include the following, User registration and Profiles for seamless purchasing of tickets rather than adding payment information every time, accounts allow users to ensure that they get the tickets they want before anyone else. Online Ticket Sales allow users to browse upcoming local events, select seats and purchase the tickets online, and integrate secure transactions with common payment gateways. The app allows users to receive emails about up and coming events and sales. Real time analytics allows the Admin to track seat sales, attendance and revenue in real time, and also allows the investors to receive quarterly reports on how well their company is performing. Ticket tech also allows for users to sell their tickets back to the platform, to discourage ticket scalping Ticket teck will only purchase the tickets back for the original sale price.
- Your user requirements (what will users be able to do with the system),
    - The users should be able to do what the use case diagram describes, we want a functional ticketing system, similar to Ticket master or other ticketing websites. We fully understand that our app may not look and work as well as Ticketmaster as we only have a certain amount of time and we are much more limited. However the user should be able to search on our website for up and coming venues and concerts that they may want to go to. our app should be able to faciliate the wants and needs of the user. as we should be able to create and app that allows users to purchase and sell tickets. the should be able to make and account and sign up with Ticket Tech and interact with the app such that they are able to buy tickest for concerts and venues that they wish to see.
- Your functional requirements (what will the system do to support users), and non-functional requirements. If you feel that other categories of requirements are needed, you can include them.  Recall that the requirements are used not only to determine the use cases that need to be developed but also to measure the success of the project (i.e., did you implement everything that was identified during the requirements engineering phase). Consider using proto-persona or journey lines to ensure you can properly and completely visualize how a user will interact with your project.  Don't forget that you will have different categories of users.  
- Your use case diagrams with the proper level of detail describing the specific scenarios.  You will need to include your diagram as well as detailed text ![Use-Case-Diagram](../images/Ticket-Teck-UseCaseDiagram.jpg)   

    ###### Use Case - Search for Venue
    - Primary actor: Users (purchasers)
    - Scope: Concert fans / sports fans
    - Level: User goal
    - Stakeholders and interests:
        - Purchaser - wants to browse venues and find one near them.
        - Admin - wants to observe who is browsing certain venues?
    - Precondition: User must access Ticket-Tech, search function must work.
    - Minimal Guarantee: Venue or group of venues is selected and allows user to see upcoming events at venue
    - Success Guarantee: Venue or group of venues is selected and events at venues are recommended to users. 
    - Main success scenario:
        - User wants to purchase a ticket for a certain event
        - User searches for a venue or an area
        - Ticket-Tech shows the venue or venues in the given areaUser gets access to venue and can see all upcoming events and dates at a certain venue
        - User can choose events they want to purchase tickets fo
    - Extensions:
        - 2a. Venue not found in location
	    - 2a1 display simple error message stating no results found
    ###### Use Case - Search for artist:
    - Primary actor: Users (purchasers)
    - Scope: Concert fans / sports fans
    - Level: User goal
    - Stakeholders and interests:
        - Purchaser - wants to browse by artist and find the artist they want and all of their shows
        - Admin - can observe what artist are doing what shows 
    - Precondition: User must access Ticket-Tech, search function must work.
    - Minimal Guarantee: Artist selected and allows user to see upcoming events that artist is apart of 
    - Success Guarantee: artist or band is selected and events at venues are recommended to users.
    - Main success scenario:
        - User wants to purchase a ticket for a certain artist
        - User searches for an artist or a band
        - Ticket-Tech shows the venue or venues that the artist or band is a part of. in the given area User gets access to venue that the artist is at  and can see all upcoming events and dates at a certain artist/band
        - User can choose events they want to purchase tickets fo
    - Extensions:
        - 2a. Artist not found
        - 2a1 display simple error message stating no results found

    ###### Use Case Log in:
    - Primary actor: Users (purchasers)
    - Scope: Concert fans / sports fans
    - Level: User goal
    - Stakeholders and interests:
    - Purchaser - able to log into their account to be able to purchase tickets at ease and to get promotional sales 
    - Admin - can observe the people who have accounts that are purchasing tickets and when
    - Precondition: User must access Ticket-Tech, must have made an account previously
    - Minimal Guarantee: User able to login and see their account information
    - Success Guarantee: proper authentication to ensure all users can access their accounts
    - Main success scenario:
        - User wants to have an account
        - User wants to have credit card info saved for faster purchasing
        - Ticket-Tech shows the user their account and able to show users promotions and presales if they have an account
        - User able to sell their tickets back at MSRP, if they wish to do so
    - Extensions:
        - 2a. Account not found / invalid
        - 2a1 display simple error message stating no account exists or invalid login
    ###### Place order
    - Primary actor: Users (purchasers)
    - Scope: Concert fans / sports fans
    - Level: User goal
    - Stakeholders and interests:
    - Purchaser - able to place an order for their tickets 
    - Admin - can observe ticket sales, and release promotional sales
    - Precondition: User must access Ticket-Tech, and have tickets in cart
    - Minimal Guarantee: User able to place an order for their tickets they want
    - Success Guarantee: able to add tickets from a venue/ artist and place and order
    - Main success scenario:
        - User wants / found a venue they want to go to
        - User has valid payment information
        -  Ticket-Tech shows the user their cart and the tickets they placed and order in for
    - Extensions:
        - 2a. Cancel order / invalid credentials 
        - 2a1 display simple error message stating error


    ###### Use Case  - Promotional / Sales / Presales
    - Primary actor: Admin
    - Scope: Ticket-Tech promotional department
    - Level: Admin goal
    - Stakeholders and interests:
        - Purchaser: who wants to buy the promotion deal on certain tickets 
    - Precondition: User already has an account in the platform
    - Minimal Guarantee: User is able to purchase tickets on sale.
    - Success Guarantee: User bought the ticket with a promotional deal, updates users
    transaction with discounted price they bought at 
    - Main success scenario:
        - User logs into the platform and 
        - Finds the promotional section on the top
        - Clicks into it
        - Sees what the tickets are on discount
        - They can also find certain tickets by searching function
        - Proceeds the to purchase with discounted price
        - Shows the updated discounted price on users transaction
    - Extensions:
        - 2a. Venue not found in location
	        - 2a1 display simple error message stating no results found
        - 3a. Tickets sold in between selection and checkout
	        - 3a1 display error message stating tickets are already sold


#### In reviewing your requirements, the reader should clearly understand what the team is proposing to build. 

 

In addition to the pdf, update your project README.md to include the requirements details and ensure that it is committed to your repo and pushed upstream by the end of the due date (I would suggest you create a Requirements Engineering branch). This will be reviewed and feedback provided to you on your commits.  

 

### Rubric:
- Description: 2 marks

- Requirements analysis and development: 5 marks

- Use case diagram and descriptions: 5 marks

#### Total: 12 
