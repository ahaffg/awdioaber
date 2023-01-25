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

---

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


---

### Structure Plane
#### **User Stories**

![User journey](/static/images/readme/userjourney.png)

| As a/an | I want to be able to ... | So that I can... |
| :--- | :--- | :---|
| **VIEWING & NAVIGATION** |
| First Timer | Easily navigate the site | Find products/information that I am require |
| First Timer | View a category of products/filter products | Find specific items I am interested in without having to scroll through all products |
| First Timer | View more detail on products | to make an informed decision of if the item suits my requirements |
| First Timer | View my running total of purchases throughout my visit | Make sure I don't overspend & am able to track whether I meet any thresholds for site offers (e.g. free delivery) |
| First Timer | View the items I currently have selected for purchase | to enable me to check I still wish to purchase the items, or amend quantities if required |
| First Timer | View ratings for products | make informed decisions about purchasing products |
| **REGISTRATION & USER ACCOUNTS** |
| Registered User | Register for an account | Have an account with the site and view my profile |
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
| **ADMIN & STORE MANAGEMENT** |
| Admin| Add a product | Add new items to my store |
| Admin | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| Admin | Delete a product | Remove items that are no longer for sale |
| Admin | Moderate forum | Remove unsuitable posts |
| Admin | Create/read/update/delete blog posts | have full CRUD functionality over the blog |
| Admin | Create/read/update/delete registered profiles | have full CRUD functionality over registered profiles |

#### **Database Schema**

I have decided to use a relational database as this will best suit my requirements, given the type of Data that I will be using in this project. [Draw Sql](https://drawsql.app/) has been used to provide a diagram of this schema.

![Database Schema V1](/static/images/readme/drawSQL-awdio-aber-export-2023-01-23.png)

This is the first version of the Schema I intend to use for the project. I decided to focus on the sales aspect of the app and ensure that was all running correctly before building the "Hire" functionality, though I expect this to work in a similar way to a "Wishlist" function. The profile schema will pull username and email data from the registration database. Potentially this process could also be used to part autofill the order form.

---

### Skeleton Plane

#### **Wireframes**

Wireframes for the project were created using [Publisher](https://www.microsoft.com/en-us/microsoft-365/publisher)

**Base Template** - This template contains the header and footer which are used throughout the website. This template is used as a base and then other pages content will be injected into main section using django template language. The footer content on mobiles will be stacked due to width restrictions. For mobile screens, the search function will be hidden within the button, and will expand when clicked. The mobile burger on the left of the nav bar will expand to reveal further navigation options.

![Base Template Wireframe](/static/images/readme/base-template.png)

**Home Page** - The home or landing page will give people thrie first impression of the company and whats on offer. Though over time the content may be changed to represent offers, new stock or even product highlights, for the purposes of this project it will highlight the 6 main categories of products. Desktop amps, portable amps, headphones, IEMs, DAPs and DACs.

On the desktop screen the products will be stacked 3 wide, 2 wide on tablets and one on top of another for mobiles due to width restrictions, to ensure content is easily viewable and readable.

![Home Page Wireframe](/static/images/readme/home-page.png)

Register Page - The register page will allow users to register for an account with Seaside Sewing in one of two ways - registering for an account with a username/email or via a social account.

The username/email path will require users to choose a username, a password which will be entered twice to confirm the user hasn't made an error when entering the password and their email address, which again will be required to be entered twice to confirm there are no mistakes in the users input.

The social media account path will allow users to sign up for an account on Seaside Sewing by using a social media account.

Register Page Wireframe

Login Page - The login page will allow users to sign into their account with either their username, or using their linked social account.

Login Page Wireframe

Logout Page - The logout page will ask the user to confirm they wish to logout. If the user clicks the logout button they will be logged out of their account and redirected to the home page.

Log out Page Wireframe

Profile Page - The profile page displays a users default delivery information, and if they have previously made any orders using their account, their past purchases will also be displayed. The user can click on the order No for their previous orders and they will be taken to a detailed view of that previous order.

Profile Page Wireframe

Bag Page (Empty Bag) - The bag page will display the following message to users if there are no products in their bag.

Empty Bag Page Wireframe

Bag Page - When a user has items in their bag, they will be shown an image of the item, the title

Bag Page Wireframe

Wish list (empty wish list) - The wish list page will display a message to the user to let them know there are no products currently in their wish list and will give instructions on how to add a product to their wish list. There will also be a button that redirects the user to the products page.

Empty Wish list Page Wireframe

Wish list Page - The wish list page is very similar in layout to the bag page. It displays an image of the item, the title, selected size and sku for the product along with the product price. There is also has a button to remove the product from their wish list. The user can add an item from their wish list to their bag by clicking on the product which will take them to the product details page where they can select sizes and quantity.

Wish list Page Wireframe

Checkout Page - The checkout page requires the user to fill in their details, along with a delivery address. They are given the option via a checkbox to save the information they input to their profile. If the user has already filled in their information in their profile, the form will be pre-populated with this information.

Underneath the users delivery information will be the payment input where the user will be required to enter their card information. If there are any errors with this input, an error message will be displayed under the input. Beneath this are the complete order buttons (which has a small message underneath it to let the user know the amount being charged to their card) and a button which redirects users back to their bag to amend their order.

The user will also be shown a summary of the products they are purchasing. This consists of an image of the product, the title of the product, a size if applicable, the quantity they are purchasing and the subtotal for that product. Underneath the summary are the subtotal, delivery costs and grand total.

Checkout Page Wireframe

Payment Processing Overlay - once the user has submitted correct payment details and clicks on the button to complete their order a payment processing overlay with an animated spinner will be displayed over the checkout page while payment is processed. Once this has processed, the user will be shown the checkout success page.

Payment Processing Overlay Wireframe

Checkout Success - The checkout success page will give the user their order details, showing the order number, the date and time of the order and the items purchased.

Checkout Success Page Wireframe

Products - The products page will display an image for each item along with the title for item, price, category and rating underneath. Screen size will determine how many products are displayed in a row.

Products Page Wireframe

Products (Admin View) - The Admin view of the products page is identical to that for a user, except for the addition of an edit and delete button below each item. This will allow the admin to be able to edit or delete products easily from the products view page.

Products Admin View Page Wireframe

Product Detail - The product detail page features an image of the product, along with the title, price, category and rating for the product.

There is also a text description of the product which gives further information to the user to enable them to decide if the product meets their needs.

Underneath the description is a quantity box for the user to select how many of the product they would like to purchase, along with an add to wish list button.

The Add to bag button and back to products buttons are placed below.

Product Detail Page Wireframe

Product Detail (Admin View) - The admin view of the product detail page is identical to the product detail page, except for the addition of the edit and delete buttons to allow the admin to edit and delete a product directly from their details page.

Product Detail Page Admin View Wireframe

Edit Product - The Edit product page is only available to admin users. It displays a form with the products details pre-populated ready for the admin to edit. The admin may also delete the current image or choose a new image to upload and display.

Edit Product Page Wireframe

Delete Product - The Delete product page is only available to admin users. Its displays the product image, title, category and SKU along with a message asking the admin if they are sure they want to delete the product. It also warns them that this action cannot be undone. They are given a cancel button and a delete button.

Delete Product Page Wireframe

404 Error - The 404 page lets the user know there has been a problem and displays a button to redirect them to the products.

404 Error Page Wireframe

Privacy Policy - The privacy policy page contains the privacy policy for the site.

Privacy Policy Page Wireframe

Terms & Conditions - The terms & conditions page contains the terms and conditions for the site.

Terms & Conditions Page Wireframe

Delivery Information - The delivery page contains further information for the user on delivery options.

Delivery Information Page Wireframe

Add review - If a user wants to add a review for a product, they will be redirected to the add review page. This will display the name of the product along with an image they would like to review. They are then given an input field to create a title for their review and a text area for the actual review. Underneath this will be a rating for the product along with a cancel and submit review button.

Add Review Page Wireframe

Toasts - Toasts are used to display messages to the user depending on their actions on the site. They can let users know if an action has been successful, if there has been an error or for displaying a general message. This is also reflected in the colour at the top of the toast. Toasts will also be used to display to a user what they currently have in their bag when they add a new product. Toasts can be dismissed by clicking the X on the toast.

Toasts Wireframe

---

## Surface Plane
### **Colour Scheme**

The aesthetic for the website is going to be far more masculine than in previous projects.  I designed the logo using [Publisher](https://www.microsoft.com/en-us/microsoft-365/publisher) and is a play on electricity and soundwaves. I'm really keen for the site to maintain high levels of accesibility, so colors will be kept to a minimum and will have a high level of contrast.


![Surface Plane](/static/images/readme/surface-plane.png)


I used [Fontjoy](https://fontjoy.com) to help me pick fonts. [Megrim](https://fonts.google.com/specimen/Megrim) will be used as the Logo font as I really love its retro/futuristic feel but would be too hard to read if used widely. [Dosis](https://fonts.google.com/specimen/Dosis) will be used for any header text as I like its stylish look across a range of weight, as well as it being easy to read. [Ubuntu](https://fonts.google.com/specimen/Ubuntu) will be used for any body text. I feel it pairs really well with Dosis and is very easy to read. Text will mostly be black, with some use of grey ensuring that it is still readable and high contrast.

![Fontjoy](/static/images/readme/fontjoy.png)

---