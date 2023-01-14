# Awdio Aber
## Backstory
For my fourth Milestone project with Code Institute I want to create a n app that will really push me outside of my comfort zone and show my ability to create solutions to problems outside my immediate field of knowledge.
My father gave me the initial seed of an idea that I should build an app for my husband. So, from there, this is how the idea had grown.

My husband is an audiophile. This means that he ~~spends all our savings on expensive MP3players~~ collects, tests and reviews audio equipment. Over the past few years he has built up a global network of contacts with audio companies and manufacturers, professional reviewers and journalists and members of the music industry.  
His primary hub for this has been [Head-Fi](https://www.head-fi.org/), a forum for audio enthusiasts. Here this community exchange opinions on equipment and over time, if (like my husband) their opinions are trusted and respected, they are often approached to review equipment on behalf of companies such as Bang and Olufsen or for their advice on equipment by musicians. *ahem* Nine Inch Nails *ahem*.

I seem to forever be posting and receiving equipment for my husband to the point where it feels like our home is part of an audio equipment conveyor belt! Members of this community are always swapping equipment as a sort of informal “try before you buy” arrangement. We especially are challenged by our location (living in far west Wales) and are unable to pop to a local audio shop to browse or buy. Also, sites like Amazon and Ebay are not ideal for selling as the second-hand market is treacherous for sellers with the risk of unhappy customers and high commission costs.

To that end, based on what I see as an opportunity within this community and driven by my husband’s knowledge and passion, I want to build an app that would allow my husband to establish as formal membership programme whereby members could sign up to hire equipment either to buy or just to try.

## Contents
---
* [User Experience](#user-experience)
  * [Strategy Plane](#strategy-plane)
    * [Project Goals](#project-goals)
  * [Scope Plane](#scope-plane)
    * [Feature Planning](#feature-planning)
  * [Structure Plane](#structure-plane)
    * [User Stories](#user-stories)
    * [Database Schema](#database-schema)
  * [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
  * [Surface Plane](#surface-plane)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
    * [Base Mockup](#base-mockup)
* [Features](#features)
  * [General Features of The Site](#general-features-of-of-the-site)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Database Used](#database-used)
  * [Frameworks Used](#frameworks-used)
  * [Libraries & Packages Used](#libraries--packages-used)
  * [Programs Used](#programs-used)
  * [Stripe](#stripe)
* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Testing](#testing)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

## User Experience
---
### Strategy Plane
#### **Project Goals**
Awdio Aber is a Business to Consumer (B2C) e-commerce site.

The sites primary audience will be audiophiles, largely men in the 25+ age range. It will cater to beginners through to experts, by selling and hiring a range of equiptment over different price points. 

Awdio Aber aims to allow customers to engage with the website on different levels through browsing, buying, reading and posting on a forum, reading blogs or becoming a member to hire equipment. It aims to establish a community that is trusted for its reviews and opinions, as well as allowing them to buy or hire equipment all on one website.

### Scope Plane

#### **Feature Planning**

Below is a table of opportunities for the project, together with a score of their importance level and viability (rated low to high, 1-5). Products that score highly on importance and viability will be features that must be addressed first as part of the MVP. Features that are scored mid range are should have features, which will be added to the project once it has achieved MVP status. Low scored features, are could have features and if not attended to in this development version will be marked to be addressed in a future version.

| Feature | Importance | Viability |  | Delivered |
| :--- | :---: | :---: | :---: | :---: |
| User roles | 5 | 5 | MVP |  |
| Sign up for an account | 4 | 5 | MVP |  |
| Account Profile | 4 | 5 | MVP |  |
| Password recovery | 5 | 5 | MVP |  |
| Use social media to sign up/log in | 2 | 4 | | |
| Search and filter through products | 5 | 5 | MVP |  |
| Checkout system | 5 | 5 | MVP |  |
| Guest Checkout | 3 | 4 | |  |
| Payment Via Stripe | 5 | 5 | MVP |  |
| Receive email confirmation for order | 5 | 5 | MVP | |
| Order History | 4 | 5 | |  |
| Admin - add product | 5 | 5 | MVP |  |
| Admin - edit/update product | 5 | 5 | MVP |  |
| Admin - delete product | 5 | 5 | MVP |  |
| Admin - Basic Stock management | 2 | 3 | |  |
| Admin - Sales Reporting | 1 | 2 | | |
| Terms and Conditions | 3 | 5 | |  |
| Privacy Policy | 3 | 5 | |  |
| Delivery Terms | 3 | 5 | |  |
| Social Media Links | 3 | 5 | |  |
| Contact form | 3 | 3 | |  |
| Wishlist | 3 | 3 | | |
| Product Reviews | 3 | 4 | | |
| Blog | 1 | 3 |  | |
| Forum | 1 | 3 |  | |


### Structure Plane
#### **User Stories**

![User journey](/static/images/readme/userjourney.png)

First time visitor.
- I want to be able to easily navigate the site.
- I want to be able to browse, search and potentially buy equipment on offer.
- I want to be able to view membership details, FAQs and be able to easily contact site admin should I have further questions.

Return visitor.
- I want to be able to create an account to read reviews by other members as well as post my own.
- I want to be able to sign up and become a member to hire equipment.
- I want to be able to review my profile and membership details.

Admin.
- I want to be able to manage any issues relating to membership and provide a quality service in a timely manner.
- I want to be able to add and remove items for sale or hire.
- I want o be able to offer and take secure payments.
- I want to be able to moderate any forum issues.

| As a/an | I want to be able to ... | So that I can... |
| :--- | :--- | :---|
| **VIEWING & NAVIGATION** |
| First Timer | Easily navigate the site | Find products/information that I am require |
| First Timer | View blog posts | Read reviews and opinions from the site owner |
| First Timer | View forum posts | Read reviews and opinions from site members |
| First Timer | Find and read TCs, FAQs and Membership info | Find answers to any queries I might have without registration |
| **SHOPPING** |
| Shopper | View individual product details | so that I can identify price, product description, product rating and the product image. |
| Shopper | View a category of products/filter products | Find specific items I am interested in without having to scroll through all products |
| Shopper | View ratings for products | make informed decisions about purchasing products |
| Shopper | View more detail on products | to make an informed decision to see if the item suits my requirements |
| Shopper | View my running total of purchases throughout my visit | Make sure I don't overspend & am able to track whether I meet any thresholds for site offers (e.g. free delivery) |
| Shopper | View the items I currently have selected for purchase | to enable me to check I still wish to purchase the items, or amend quantities if required |
| **SORTING & SEARCHING** |
| Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sort products |
| Shopper | Sort a specific category of products | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories, such as DAPs or headphones |
| Shopper | Search for a product by name or description | Find a specific product I'd like to purchase |
| Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |
| **PURCHASING & CHECKOUT** |
| Shopper | Easily select the quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product quantity |
| Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive |
| Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout |
| Shopper | Easily enter my payment information | Check out quickly and with no hassles |
| Shopper | Know my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase |
| Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |
| **REGISTRATION & USER ACCOUNTS** |
| Registered User | Register for an account | Have an account with the site and view my profile |
| Registered User | Register for an account using social media| use social media accounts to speed up registration and use google or apple pay |
| Registered User | Receive an email to confirm my registration | Verify my account was created successfully |
| Registered User | Log in and out | Keep my account information secure |
| Registered User | View a profile page | Set a default delivery address and view previous purchases |
| Registered User | Reset my password | Recover my account |
| Registered User | Create/read/update/delete forum posts | have full CRUD functionality over my forum posts |
| **MEMBER ACCOUNTS** |
| Member | Register for a member account account | Have an account with the site and view my profile |
| Member | Easily enter my payment information | Check out quickly and with no hassles |
| Member | Know my personal and payment information is safe and secure | Confidently provide the needed information to become a member |
| Member | Sort the list of available products by name or category | Easily identify the best rated, best priced and categorically sort products |
| Member | "Book" my desired product | View item in my bag to be hired |
| Member | View an order confirmation after booking | Verify that I haven't made any mistakes |
| Member | Receive an email confirmation after booking | Keep the confirmation of what I've hired for my records | 
| **ADMIN & STORE MANAGEMENT** |
| Admin| Add a product | Add new items to my store |
| Admin | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| Admin | Delete a product | Remove items that are no longer for sale |
| Admin | Moderate forum | Remove unsuitable posts |
| Admin | Create/read/update/delete blog posts | have full CRUD functionality over the blog |
| Admin | Create/read/update/delete registered profiles | have full CRUD functionality over registered profiles |


