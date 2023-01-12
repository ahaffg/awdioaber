## Backstory
For my fourth Milestone project with Code Institute I want to create a n app that will really push me outside of my comfort zone and show my ability to create solutions to problems outside my immediate field of knowledge.
My father gave me the initial seed of an idea that I should build an app for my husband. So, from there, this is how the idea had grown.

My husband is an audiophile. This means that he ~~spends all our savings on expensive MP3players~~ collects, tests and reviews audio equipment. Over the past few years he has built up a global network of contacts with audio companies and manufacturers, professional reviewers and journalists and members of the music industry.  
His primary hub for this has been [Head-Fi](https://www.head-fi.org/), a forum for audio enthusiasts. Here this community exchange opinions on equipment and over time, if (like my husband) their opinions are trusted and respected, they are often approached to review equipment on behalf of companies such as Bang and Olufsen or for their advice on equipment by musicians. *ahem* Nine Inch Nails *ahem*.

I seem to forever be posting and receiving equipment for my husband to the point where it feels like our home is part of an audio equipment conveyor belt! Members of this community are always swapping equipment as a sort of informal “try before you buy” arrangement. We especially are challenged by our location (living in far west Wales) and are unable to pop to a local audio shop to browse or buy.
Also, sites like Amazon and Ebay are not ideal for selling as the second-hand market is treacherous for sellers with the risk of unhappy customers and high commission costs.
To that end, based on what I see as an opportunity within this community and driven by my husband’s knowledge and passion, I want to build an app that would allow my husband to establish as formal membership programme whereby members could sign up to hire equipment either to buy or just to try.



## Contents

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


## Structure Plane
### User Stories

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

| User Story | As a/an | I want to be able to ... | So that I can... |
| :--- | :--- | :--- | :---|
| **VIEWING & NAVIGATION** |
| 1 | First Timer | Easily navigate the site | Find products/information that I am require |
| 2 | First Timer | View a category of products/filter products | Find specific items I am interested in without having to scroll through all products |
| 3 | First Timer | View more detail on products | to make an informed decision of if the item suits my requirements |
| 4 | First Timer | View items on clearance/sale easily | Save money  |
| 5 | First Timer | View my running total of purchases throughout my visit | Make sure I don't overspend & am able to track whether I meet any thresholds for site offers (e.g. free delivery) |
| 6 | First Timer | View the items I currently have selected for purchase | to enable me to check I still wish to purchase the items, or amend quantities if required |
| 7 | First Timer | View ratings for products | make informed decisions about purchasing products |
| **REGISTRATION & USER ACCOUNTS** |
| 8 | Shopper | Register for an account | Have an account with the site and view my profile |
| 9 | Shopper | Receive an email to confirm my registration | Verify my account was created successfully |
| 10 | Shopper | Log in and out | Keep my account information secure |
| 11 | Shopper | View a profile page | Set a default delivery address and view previous purchases |
| 12 | Shopper | Reset my password | Recover my account |
| **SORTING & SEARCHING** |
| 13 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sort products |
| 14 | Shopper | Sort a specific category of products | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| 15 | Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories, such as fabric or haberdashery |
| 16 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase |
| 17 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |
| **PURCHASING & CHECKOUT** |
| 18 | Shopper | Easily select the quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product quantity |
| 19 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive |
| 20 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout |
| 21 | Shopper | Easily enter my payment information | Check out quickly and with no hassles |
| 22 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase |
| 23 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| 24 | Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |
| **ADMIN & STORE MANAGEMENT** |
| 25 | Store Owner | Add a product | Add new items to my store |
| 26 | Store Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| 27 | Store Owner | Delete a product | Remove items that are no longer for sale |


