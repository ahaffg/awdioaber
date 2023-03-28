# Code Institute - Level 5 Diploma in Web Application Development - Milestone Project 4
# Awdio Aber
![Awdio Aber Mockup](/media/all-devices-black%20(1).png)

## Backstory
For my fourth Milestone project with Code Institute I want to create a n app that will really push me outside of my comfort zone and show my ability to create solutions to problems outside my immediate field of knowledge.
My father gave me the initial seed of an idea that I should build an app for my husband. So, from there, this is how the idea had grown.

My husband is an audiophile. This means that he ~~spends all our savings on expensive MP3players~~ collects, tests and reviews audio equipment. Over the past few years he has built up a global network of contacts with audio companies and manufacturers, professional reviewers and journalists and members of the music industry.

His primary hub for this has been [Head-Fi](https://www.head-fi.org/), a forum for audio enthusiasts. Here this community exchange opinions on equipment and over time, if (like my husband) their opinions are trusted and respected, they are often approached to review equipment on behalf of companies such as Bang and Olufsen or for their advice on equipment by musicians. *ahem* Nine Inch Nails *ahem*.

I seem to forever be posting and receiving equipment for my husband to the point where it feels like our home is part of an audio equipment conveyor belt! Members of this community are always swapping equipment as a sort of informal “try before you buy” arrangement. We especially are challenged by our location (living in far west Wales) and are unable to pop to a local audio shop to browse or buy. Also, sites like Amazon and Ebay are not ideal for selling as the second-hand market is treacherous for sellers with the risk of unhappy customers and high commission costs.

To that end, based on what I see as an opportunity within this community and driven by my husband’s knowledge and passion, I want to build an app that would allow my husband to establish as formal membership programme whereby members could sign up to hire equipment either to buy or just to try.

The live site can be seen [here](https://awdioaber.herokuapp.com/).

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

**Register Page** - The register page will allow users to register for an account in one of two ways - registering for an account with a username/email or via a social account.

The username/email path will require users to choose a username, a password which will be entered twice to confirm the user hasn't made an error when entering the password and their email address, which again will be required to be entered twice to confirm there are no mistakes in the users input.

The social media account path will allow users to sign up for an account by using a social media account.

![Register Page Wireframe](/static/images/readme/register-page.png)

**Login Page** - The login page will allow users to sign into their account with either their username, or using their linked social account.

![Login Page Wireframe](/static/images/readme/login-page.png)

**Logout Page** - The logout page will ask the user to confirm they wish to logout. If the user clicks the logout button they will be logged out of their account and redirected to the home page.

![Log out Page Wireframe](/static/images/readme/logout-page.png)

**Profile Page** - The profile page displays a users default delivery information, and if they have previously made any orders using their account, their past purchases will also be displayed. The user can click on the order No for their previous orders and they will be taken to a detailed view of that previous order.

![Profile Page Wireframe](/static/images/readme/profile-page.png)

**Bag Page (Empty Bag)** - The bag page will display the following message to users if there are no products in their bag.

![Empty Bag Page Wireframe](/static/images/readme/empty-bag-page.png)

**Bag Page** - When a user has items in their bag, they will be shown an image of the item, the title, price and ammount that the user has ordered. There is an option to edit the ammount or delete the product, as well as buttons to either return you to the shopping page or on to the checkout page.

![Bag Page Wireframe](/static/images/readme/bag-page.png)

**Checkout Page** - The checkout page requires the user to fill in their details, along with a delivery address. They are given the option via a checkbox to save the information they input to their profile. If the user has already filled in their information in their profile, the form will be pre-populated with this information.

Underneath the users delivery information will be the payment input where the user will be required to enter their card information. If there are any errors with this input, an error message will be displayed under the input. Beneath this are the complete order buttons (which has a small message underneath it to let the user know the amount being charged to their card) and a button which redirects users back to their bag to amend their order.

The user will also be shown a summary of the products they are purchasing. This consists of an image of the product, the title of the product, a size if applicable, the quantity they are purchasing and the subtotal for that product. Underneath the summary are the subtotal, delivery costs and grand total.

![Checkout Page Wireframe](/static/images/readme/checkout.png)

**Payment Processing Overlay** - once the user has submitted correct payment details and clicks on the button to complete their order a payment processing overlay with an animated spinner will be displayed over the checkout page while payment is processed. Once this has processed, the user will be shown the checkout success page.

![Payment Processing Overlay Wireframe](/static/images/readme/checkout-overlay.png)

**Checkout Success** - The checkout success page will give the user their order details, showing the order number, the date and time of the order and the items purchased.

![Checkout Success Page Wireframe](/static/images/readme/success.png)

**Products** - The products page will display an image for each item along with the title for item, price, category and rating underneath. Screen size will determine how many products are displayed in a row.

![Products Page Wireframe](/static/images/readme/products.png)

**Products (Admin View)** - The Admin view of the products page is identical to that for a user, except for the addition of an edit and delete button below each item. This will allow the admin to be able to edit or delete products easily from the products view page.

![Products Admin View Page Wireframe](/static/images/readme/products-admin.png)

**Product Detail** - The product detail page features an image of the product, along with the title, price, category and rating for the product.

There is also a text description of the product which gives further information to the user to enable them to decide if the product meets their needs.

Underneath the description is a quantity box for the user to select how many of the product they would like to purchase, along with an add to wish list button.

The Add to bag button and back to products buttons are placed below.

![Product Detail Page Wireframe](/static/images/readme/product-detail.png)

**Product Detail (Admin View)** - The admin view of the product detail page is identical to the product detail page, except for the addition of the edit and delete buttons to allow the admin to edit and delete a product directly from their details page.

![Product Detail Page Admin View Wireframe](/static/images/readme/product-detail-admin.png)

**Edit Product** - The Edit product page is only available to admin users. It displays a form with the products details pre-populated ready for the admin to edit. The admin may also delete the current image or choose a new image to upload and display.

![Edit Product Page Wireframe](/static/images/readme/productedit.png)

**Delete Product** - The Delete product page is only available to admin users. Its displays the product image, title, category and SKU along with a message asking the admin if they are sure they want to delete the product. It also warns them that this action cannot be undone. They are given a cancel button and a delete button.

![Delete Product Page Wireframe](/static/images/readme/product-delete.png)

**404 Error** - The 404 page lets the user know there has been a problem and displays a button to redirect them to the products.

![404 Error Page Wireframe](/static/images/readme/404.png)

**Privacy Policy** - The privacy policy page contains the privacy policy for the site.

![Privacy Policy Page Wireframe](/static/images/readme/privacy-policy.png)

**Terms & Conditions** - The terms & conditions page contains the terms and conditions for the site.

![Terms & Conditions Page Wireframe](/static/images/readme/tncs.png)

**Delivery Information** - The delivery page contains further information for the user on delivery options.

![Delivery Information Page Wireframe](/static/images/readme/shipping.png)

**Add review** - If a user wants to add a review for a product, they will be redirected to the add review page. This will display the name of the product along with an image they would like to review. They are then given an input field to create a title for their review and a text area for the actual review. Underneath this will be a rating for the product along with a cancel and submit review button.

![Add Review Page Wireframe](/static/images/readme/review.png)

**Toasts** - Toasts are used to display messages to the user depending on their actions on the site. They can let users know if an action has been successful, if there has been an error or for displaying a general message. This is also reflected in the colour at the top of the toast. Toasts will also be used to display to a user what they currently have in their bag when they add a new product. Toasts can be dismissed by clicking the X on the toast.

![Toasts Wireframe](/static/images/readme/toast.png)

---

## Surface Plane
### **Colour Scheme**

The aesthetic for the website is going to be far more masculine than in previous projects.  I designed the logo using [Publisher](https://www.microsoft.com/en-us/microsoft-365/publisher) and is a play on electricity and soundwaves. I'm really keen for the site to maintain high levels of accesibility, so colors will be kept to a minimum and will have a high level of contrast.


![Surface Plane](/static/images/readme/surface-plane.png)


I used [Fontjoy](https://fontjoy.com) to help me pick fonts. [Megrim](https://fonts.google.com/specimen/Megrim) will be used as the Logo font as I really love its retro/futuristic feel but would be too hard to read if used widely. [Dosis](https://fonts.google.com/specimen/Dosis) will be used for any header text as I like its stylish look across a range of weight, as well as it being easy to read. [Ubuntu](https://fonts.google.com/specimen/Ubuntu) will be used for any body text. I feel it pairs really well with Dosis and is very easy to read. Text will mostly be black, with some use of grey ensuring that it is still readable and high contrast.

![Fontjoy](/static/images/readme/fontjoy.png)

### **Imagery**

The images used for this site have been taken from [Headfonics](https://headfonics.com). The reason I chose this website was because their product photograpy is excelent! They are fantastic high quality images, with large clean backgrounds, allowing for focus on the products themselves and giving a really streamlined proffessional feel to the site.

I will also adapt text from their reviews to provide product descriptions and ratings for this site.

![Imagery](/static/images/readme/imagery.png)

Although the Site will look largely the same across all media sizes there will be some differences as a result of the screen widths available. For example, Products will stack on mobile, be side-by-side on small and medium screens, split into three columns on large and four columns on extra-large.

**Mobile Site** - It is likely that the image used for the head hero image will be different due to the smaller width space available. I will adapt this image accordingly and use media queries to allow for the need for different sized images to be used.

Content will be largely stacked one on top of another so that it remains accesible. The footer image may be left as a text-logo instead of a photo-image- depending on size and how it looks on-screen.

**Tablet Site**  -  As tablets offer wider screens, this will give me the opportunity to have a hero image that is more spacious, adding to the overall sleek look of the site. It is likely that this image will be repeated or a similar image used as the footer.

Depending on the content, images and text may be doubled on screen. Like the mobile site, the menu will appear as a hamburger on the left hand side, as well as short-cuts to search, login and shopping bag functions being represented by anchored icons on the right hand side of the nav area.

**Desktop Site** - On the desktop site, the photography will be shown off to it's best advantage, with large images, and lots of white-space to allow the products to stand out.

The Nav area will look slightly different with the text logo placed in the top-left hand corner, with the clickable login and bag items in the right hand corner. The search bar however will be permenently accesableat the top center of the screen no matter what page is open.

If at all possible I would really like to find a way for the hero images to change every time the page is refreshed. I would also like to include the hero-zoom animation from the [Love Running](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CSE101+2020_Q2/courseware/be0e510a3aca4bccb6e0bba4cf7cf06b/15fe9d557bcc4af5a117465b9150454f/) project. I think this would add a nice touch to the site and further seperate it from the [Boutique Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/) site.

**Base Mockup**

![Base Mockup](/static/images/readme/base-mockup.png)

---
## Features

### General Features of of the site

Each page of the site shares the following:

* Favicon - I used [Favicon.io](https://favicon.io/) to create the favicon for the site.

![Favicon](/static/images/readme/favicon_io.png)

* Navbar - The navbar on the site is split into two sections, the first section contains the search bar, an account icon and the bag icon. The second section contains the sites products categories. The navbar is fully responsive, and utilises a hamburger menu toggle on smaller screens.

![Navbar](/static/images/readme/navbar-toggle.png)

* Banner Ticker - The code for the banner ticker has been adapted from [Code-Boxx](https://code-boxx.com/html-css-news-ticker-horizontal-vertical/) and I feel helps the site feel more dynamic. The code allows for messages to be rotated through the banner continuously. I like that the imformation can be changed regularly, even providing links, giving users an opertunity to see wider aspects of the store.

![Banner Ticker](/static/images/readme/ticker-banner.png)

---

## Technologies Used

### Languages Used

HTML, CSS, JavaScript, Python.

### Database Used

sqlite3 for development.

[ElephantSQL](https://www.elephantsql.com/) for deployment.

### Frameworks Used

[Django](https://www.djangoproject.com/) - Version 3.2.16 - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Version 4.6.2 - A framework for building responsive, mobile-first sites.

### Libraries & Packages Used

[jQuery](https://jquery.com/) - Version 3.6.2 - A JavaScript Framework

[Font Awesome](https://fontawesome.com/) - Version 6.2.1 - Used for the iconography of the site, this was added using a CDN link.

[Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Version 0.41.0 - Used for authentication, registration & account management.

[django-countries](https://pypi.org/project/django-countries/7.2.1/) - Version 7.2.1 - This is the latest stable version that is compatible with GitPod.

[django_crispy_forms](https://pypi.org/project/django-crispy-forms/) - provides a tag and filter that lets you quickly render forms

[gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server

[pillow](https://pypi.org/project/Pillow/) - Python imaging library

[dj_databsae_url](https://pypi.org/project/dj-database-url/) - allows us to utilise the DATABASE_URL variable

[psycopg2](https://pypi.org/project/psycopg2/) - a postgres database adapter which allow us to connect with a postgres database

[django-storages](https://pypi.org/project/django-storages/) - a storage backend library

[magnify.js](https://thdoan.github.io/magnify/) - Used to add the magnify lens to the product details product image

### Programs Used

[DrawSQL.app](https://drawsql.app/) - Used to create the database schema.

[Favicon.io](https://favicon.io/) - To create the favicon.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store the files for this project.

[Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot, test features and solve issues with responsiveness and styling.

[Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.

### Stripe

[Stripe](https://stripe.com/gb) has been used in the project to implement the payment system.

Stripe for the website is currently in developer mode, which allows us to be able to process test payments to check the function of the site.

---

## Deployment & Local Development

### Deployment

The project is deployed using Heroku. To deploy the project:

#### **Create the Live Database**

We have been using the sqlite3 database in development, however this is only available for use in development so we will need to create a new external database which can be accessed by Heroku.

1. Go to the [ElephantSQL](https://www.elephantsql.com/) dashboard and click the create new instance button on the top right.
2. Name the plan (your project name is a good choice), select tiny turtle plan (this is the free plan) and choose the region that is closest to you then click the review button.
3. Check the details are all correct and then click create instance in the bottom right.
4. Go to the dashboard and select the database just created.
5. Copy the URL (you can click the clipboard icon to copy)

#### **Heroku app setup**

  1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the new button in the top right corner and select create new app.
  2. Give your app a name (this must be unique), select the region that is closest to you and then click the create app button bottom left.
  3. Open the settings tab and create a new config var of `DATABASE_URL` and paste the database URL you copied from elephantSQL into the value (the value should not have quotation marks around it).

#### **Preparation for deployment in GitPod**

1. Install dj_database_url and psycopg2 (they are both needed for connecting to the external database you've just set up):

   ```bash
   pip3 install dj_database_url==0.5.0 psycopg2
   ```

2. Update your requirements.txt file with the packages just installed:

    ```bash
    pip3 freeze > requirements.txt
    ```

3. In settings.py underneath import os, add `import dj_database_url`

4. Find the section for DATABASES and comment out the code. Add the following code below the commented out database block, and use the URL copied from elephantSQL for the value:

    (NOTE! don't delete the original section, as this is a temporary step whilst we connect the external database. Make sure you don't push this value to GitHub - this value should not be saved to GitHub, it will be added to the Heroku config vars in a later step, this is temporary to allow us to migrate our models to the external database)

    ```python
    DATABASES = {
        'default': dj_database_url.parse('paste-elephantsql-db-url-here')
    }
    ```

5. In the terminal, run the show migrations command to confirm connection to the external database:

    ```bash
    python3 manage.py runserver
    ```

6. If you have connected the database correctly you will see a list of migrations that are unchecked. You can now run migrations to migrate the models to the new database:

    ```bash
    python3 manage.py migrate
    ```

7. Create a superuser for the new database. Input a username, email and password when directed.

    ```bash
    python3 manage.py createsuperuser
    ```

8. You should now be able to go to the browser tab on the left of the page in elephantsql, click the table queries button and see the user you've just created by selecting the auth_user table.
9. We can now add an if/else statement for the databases in settings.py, so we use the development database while in development (the code we commented out) - and the external database on the live site (note the change where the db URL was is now a variable we will use in Heroku):

    ```python
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
          'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
          }
        }
    ```

10. Install gunicorn which will act as our webserver and freeze this to the requirements.txt file:

    ```bash
    pip3 install gunicorn
    pip3 freeze > requirements.txt
    ```

11. Create a `Procfile` in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves our django app. Add the following to the file (making sure not to leave any blank lines underneath):

    ```Procfile
    web: gunicorn seaside_sewing.wsgi:application
    ```

12. Log into the Heroku CLI in the terminal and then run the following command to disable collectstatic. This command tells Heroku not to collect static files when we deploy:

    ```bash
    heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
    ```

13. We will also need to add the Heroku app and localhost (which will allow GitPod to still work) to ALLOWED_HOSTS = [] in settings.py:

    ```python
    ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
    ```

14. Save, add, commit and push the changes to GitHub. You can then also initialize the Heroku git remote in the terminal and push to Heroku with:

    ```bash
    heroku git:remote -a {app name here}
    git push heroku master
    ```

15. You should now be able to see the deployed site (without any static files as we haven't set these up yet).

16. To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect. Click enable automatic deploys at the bottom of the page.

#### **Generate a SECRET KEY & Updating Debug**

1. Django automatically sets a secret key when you create your project, however we shouldn't use this default key in our deployed version, as it leaves our site vulnerable. We can use a random key generator to create a new SECRET_KEY which we can then add to our Heroku config vars which will then keep the key protected.
2. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) is an example of a site we could use to create our secret key. Create a new key and copy the value.
3. In Heroku settings create a new config var with a key of `SECRET_KEY`. The value will be the secret key we just created. Click add.
4. In settings.py we can now update the `SECRET_KEY` variable, asking it to get the secret key from the environment, or use an empty string in development:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
    ```

5. We can now adjust the `DEBUG` variable to only set DEBUG as true if in development:

    ```python
    DEBUG = 'DEVELOPMENT' in os.environ
    ```

6. Save, add, commit and push these changes.

#### **Set up AWS hosting for static and media files**

! NOTE: These instructions are for setting up AWS hosting as of 5/1/23 - these may change slightly in future versions of AWS.

1. Sign up or login to your [aws amazon account](https://aws.amazon.com) on the top right by using the manage my account button and then navigate to S3 to create a new bucket.
2. The bucket will be used to store our files, so it is a good idea to name this bucket the same as your project. Select the region closest to you. In the object ownership section we need to select ACLs enabled and then select bucket owner preferred. In the block public access section uncheck the block public access box. You will then need to tick the acknowledge button to make the bucket public. Click create bucket.
3. Click the bucket you've just created and then select the properties tab at the top of the page. Find the static web hosting section and choose enable static web hosting, host a static website and enter index.html and error.html for the index and error documents (these won't actually be used.)
4. Open the permissions tab and copy the ARN (amazon resource name). Navigate to the bucket policy section click edit and select policy generator. The policy type will be S3 bucket policy, we want to allow all principles by adding `*` to the input and the actions will be get object. Paste the ARN we copied from the last page into the ARN input and then click add statement. Click generate policy and copy the policy that displays in a new pop up. Paste this policy into the bucket policy editor and make the following changes: Add a `/*` at the end of the resource value. Click save.
5. Next we need to edit the the cross-origin resource sharing (CORS). Paste in the following text:

    ```json
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```

6. Now we need to edit the access control list (ACL) section. Click edit and enable list for everyone(public access) and accept the warning box.

#### **Creating AWS groups, policies and users**

1. Click the services icon on the top right of the page and navigate to IAM - manage access to AWS services. On the left hand navigation menu click user groups and then click the create group button in the top right. This will create the group that our user will be placed in.
2. Choose a name for your group - for example manage-seaside-sewing, and click the create policy button on the right. This will open a new page.
3. Click on the JSON tab and then click the link for import managed policy on the top right of the page.
4. Search for S3 and select the one called AmazonS3FullAccess, then click import.
5. We need to make a change to the resources, we need to make resources an array and then change the value for resources. Instead of a `*` which allows all access, we want to paste in our ARN. followed by a comma, and then paste the ARN in again on the next line with `/*` at the end. This allows all actions on our bucket, and all the resources in it.
6. Click the next: tags button and then the next:review .
7. Give the policy a name and description (e.g. seaside-sewing-policy | Access to S3 bucket for seaside sewing static files.) Click the create policy button.
8. Now we need to atach the policy we just created. On the left hand navigation menu click user groups, select the group and go to the permissions tab. Click the add permissions button on the right and choose attach policies from the dropdown.
9. Select the policy you just created and then click add permissions at the bottom.
10. Now we'll create a user for the group by clicking on the user link in the left hand navigation menu, clicking the add users button on the top right and giving our user a username (e.g. seaside-sewing-staticfiles-user). Select programmatic access and then click the next: permissions button.
11. Add the user to the group you just created and then click next:tags button, next:review button and then create user button.
12. You will now need to download the CSV file as this contains the user access key and secret access key that we need to insert into the Heroku config vars. Make sure you download the CSV now as you won't be able to access it again.

#### **Connecting Django to our S3 bucket**

1. Install boto3 and django storages and freeze them to the requirements.txt file.

    ```bash
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```

2. Add `storages` to the installed apps in settings.py
3. Add the following code in settings.py to use our bucket if we are using the deployed site:

    ```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }
        
        AWS_STORAGE_BUCKET_NAME = 'enter your bucket name here'
        AWS_S3_REGION_NAME = 'enter the region you selected here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```

4. In Heroku we can now add these keys to our config vars:

    | KEY | VALUE |
    | :--- | :--- |
    | AWS_ACCESS_KEY_ID | The access key value from the amazon csv file downloaded in the last section |
    | AWS_SECRET_ACCESS_KEY | The secret access key from the amazon csv file downloaded in the last section |
    | USE_AWS | True |

5. Remove the DISABLE_COLLECTSTATIC variable.
6. Create a file called custom_storages.py in the root and import settings and S3Botot3Storage. Create a custom class for static files and one for media files. These will tell the app the location to store static and media files.
7. Add the following to settings.py to let the app know where to store static and media files, and to override the static and media URLs in production.

    ```python
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

8. Save, add, commit and push these changes to make a deployment to Heroku. In the build log you should be able to see that the static files were collected, and if we check our S3 bucket we can see the static folder which has all the static files in it.
9. Navigate to S3 and open your bucket. We now want to create a new file to hold all the media files for our site. We can do this by clicking the create folder button on the top right and naming the folder media.

#### **Setting up Stripe**

1. We now need to add our Stripe keys to our config vars in Heroku to keep these out of our code and keep them private. Log into Stripe, click developers and then API keys.
2. Create 2 new variables in Heroku's config vars - for the publishable key (STRIPE_PUBLIC_KEY) and the secret key (STRIPE_SECRET_KEY) and paste the values in from the Stripe page.
3. Now we need to add the WebHook endpoint for the deployed site. Navigate to the WebHooks link in the left hand menu and click add endpoint button.
4. Add the URL for our deployed sites WebHook, give it a description and then click the add events button and select all events. Click Create endpoint.
5. Now we can add the WebHook signing secret to our Heroku config variables as STRIPE_WH_SECRET.
6. In settings.py:

    ```python
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```

### Local Development

#### **How to Fork**

To fork the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [seaside-sewing](https://github.com/kera-cudmore/seaside-sewing).

3. Click on the fork button in the top right of the page.

#### **How to Clone**

To clone the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [seaside-sewing](https://github.com/kera-cudmore/seaside-sewing).

3. Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.

4. Open the terminal in your chosen IDE and change the current working directory to the location you would like to use for the cloned repository.

5. Type the following command into the terminal `git clone` followed by the link you copied in step 3.

6. Set up a virtual environment (this step is not required if you are using the Code Institute template and have opened the repository in GitPod as this will have been set up for you).

7. Install the packages from the requirements.txt file by running the following command in the terminal:

```bash
pip3 install -r requirements.txt
```

---

## Credits

### Code Used

This project was created using methods taught in the Code Institutes walkthrough project for Boutique Ado.

The code to create the image zoom on the products page was taken from [Thdoan Magnify JS](https://thdoan.github.io/magnify/)

### Content

Product descriptions for this site were adapted from reviews from [Headfonics](https://headfonics.com). Blogs have been adapted from blogs posted on [Audiophile Review](https://audiophilereview.com/) any other content was written by myself, Angharad Griffiths.

### Media

* [Headfonics](https://headfonics.com) - whose images were used throughout this website.
* [Website Mockup Generator](https://websitemockupgenerator.com/) - used for the website mockup image at the head of this readme document.
* [Merch Mockup Generator](https://mock-it.co/) - used to mock up store merch.

### Acknowledgments

I would like to acknowledge the following people who have helped me with completing this project:

* My family for their patience and support whilst working on my final project.
* My fantastic mentor Martina Terlević for always being so helpful and flexible, as well as all round awesome human!
* The Code Institute Tutors who assisted me at so many points along the way especially Ed, Oisin, Gemma and Ger, you are complete legends!