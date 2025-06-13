# CURLCULTURE

## Introduction

Curlculture is a fictional B2C e-commerce hair salon that is designed and implemented with Python and Django, HTML, CSS and some Javascript. It specialises in boking hair salon services and selling hair salon products to consumers online. the project has been inspired by a friend's existing hair salon.

Link to deployed site can be found [Here](https://curlculture-6f312b34fcce.herokuapp.com/)

## Showcase

![Home page](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749564576/curlculture_az4xhp.png)

# UX

## User stories

## As Admin

- As a admin I can manage users' accounts so that I can make any required changes to them if needed
- As a admin I can manage products so that I can add , update or delete products when necessary
- As a admin I can view created orders so that I can full fill the orders or amend if needed
- As a Admin I can delete any of comments so that I can remove them if I nolonger feel they are still necessary or needed
- As a Admin I can view messages sent via contact form so that I can act upon them

## As a site user

- As a site user I can create or edit my account so that I can update my details accordingly
- As a site user I can login in my account so that I can view my order history
- As a site user I can search for products so that I can find specific products
- As a site user I can sort products and services on criteria such as price and category so that I can I have a method of ordering the products as I prefer
- As a site user I can browse through products and services so that I can decide what I may be interested in buying
- As a site user I can look at product and services details so that I can decide if I want to purchase it
- As a site user I can easily add products I want to purchase to a cart so that I can decide whether to purchase or not
- As a site user I can view the contents of my cart so that I can be able to make any adjustments
- As a site user I can update my cart by adding more or remove products so that I can decide on the number of products I intend to buy
- As a site user I can view my order summary so that I can verify it before confirming
- As a site user I can checkout securely so that I can I maintain the level of trust on the site
- As a site user I can view all reviews so that I can decide what I may be interested in reading
- As a site user I can add a review so that I can express my opinion
- As a site user I can use the contact form so that I can contact the site owners
- As a site user I can sign up to newsletter so that I can keep updated on the latest news

## Architecture

## Database

<details>
  <summary>Click here to view Database Schema:</summary>

## Entity Relationship Diagram (ERD)

The CurlCulture website is structured around several core features: user management, salon bookings, product sales, customer engagement, and reviews. The following is a brief overview of the main data models and their relationships:
User (auth_user): Standard Django authentication is used for customer accounts, enabling login, bookings, orders, and reviews.

- Salon Services

* ServiceCategory: Organizes services (e.g., Braiding, Treatments).

* SalonService: Represents individual services with details like duration, price, and whether hair is provided.

- Bookings

* Booking: Links a user to a selected service, with date and time.

- Reviews

* Review: Allows users to rate and comment on services they’ve experienced.

- Shop

* Product: Contains items available for purchase.

* Order: Represents a purchase made by a user.

* OrderItem: Individual products and quantities within an order.

- Contact & Subscriptions

* ContactMessage: Stores customer inquiries.

* Subscriber: Tracks newsletter sign-ups.

Each model is relationally linked using foreign keys, supporting a fully connected user experience across salon services, e-commerce, and communication features.

![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749565073/erd_ewwurx.png)

  </details>

## Design

Before I wrote any code for this site, I had to pin point a simple design of what I wanted my site to look like by using wireframes, not only for myself but as well of communicating what I wanted to archieve to my mentor.

<details>
  <summary>Click here to view Wireframes:</summary>

![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749600993/Home_e9ubgo.png)
![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749600971/Bookings_izw62p.png)
![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749600999/Reviews_amifrj.png)
![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749600999/Shop_lzdzac.png)
![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749600971/Cart_bqst0s.png)
![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749600971/Checkout_spl9ez.png)
![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749600995/Register_xmi1pw.png)
![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749600994/Login_w8t7ch.png)
![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749600994/Profile_mr3yrx.png)

  </details>

## E-commerce type

CurlCulture is a hair salon that has both walk-in and bookings services, it sells hair products directly to customers. This can be done online or on site. The functionality on this site for a regular customer to be able to make a purchase swiflty and quickly. For the owners, the goal is to archieve CRUD functionality.

## Marketing

Though there are a lot of marketing techniques for businesses, Pack and Stash decided to first use the cheaper way, that is facebook to drive out content and engage with customers.

![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749601767/facebook_cc_q0ay07.png)

# Features

## Responsive Design

The site is fully responsive and works seamlessly on desktop, tablet, and mobile devices.

![](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749772821/responsive_uadmuc.png)

### User Authentication

- Users can register, log in, log out, and manage their profile.
- Secure password reset and email verification for new accounts.

![register](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749776270/register_jpix29.png)

![login](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749776260/login_tioyia.png)

### Product Catalog

- Browse all available hair products with images, descriptions, categories, and prices.
- Products can be filtered by category and sorted by price or name.
- Detailed product pages with add-to-cart functionality.

![shop](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749776438/shop_fmn0fg.png)

### Shopping Cart

- Add, update, or remove products from the cart.
- View cart summary with itemized subtotals and total cost.
- Cart persists across sessions for logged-in users.

![cart](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749776014/cart_qok9qw.png)

### Secure Checkout

- Integrated Stripe payment gateway for secure online payments.
- Order summary and shipping calculation before payment.
- Confirmation page after successful checkout.

![checkout](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749767946/checkout1_gufbqi.png)

### Salon Bookings

- Book salon services directly from the website.
- View and manage upcoming bookings in the user profile.

![bookings](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749767957/services_efgorc.png)

### Reviews

- Users can view and submit reviews for salon services.
- Reviews are displayed on relevant service pages.

![reviews](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749775700/reviews_i11d1g.png)

### Newsletter Subscription

- Users can subscribe to a newsletter to receive updates and special offers.

![newsletter](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749776521/newsletter_oybaxn.png)

### Contact Form

- Users can send messages to the salon via a contact form.
- Admins can view and respond to messages in the admin panel.

![contact](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749767947/contact_khyweq.png)

### Admin Features

- Admins can manage users, products, orders, bookings, reviews, blog posts, and contact messages through the Django admin interface.

![admin](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749774672/admin_rauftp.png)

## Privacy policy

![policy](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749767954/privacy_q1yp5q.png)

## Facebook

In terms of marketing, the site has a facebook page to push content.and target some of its customers through content creation

![facebook](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749601767/facebook_cc_q0ay07.png)

# Profile

- The user profile page gives user an option to edit or delete the account
- There is also a view booking history option

![profile](https://res.cloudinary.com/dzibrzlq9/image/upload/v1749767957/profile_hphcgo.png)

# 404 page

A 404 page is also available to handle navigation errors with a home link button to take them back to the home page

![error handling](static/images/404.jpg)

### Future features

- Admin dashboard with analytics
- Wishlist/favorites for products
- Social login (Google, Facebook)
- Product bundles and discounts

# Web marketing

## Email marketing

- CurlCulture uses Mailchimp for email marketing and newsletter management.
- New users are automatically added to the weekly newsletter, helping to nurture leads and keep customers engaged with updates, promotions, and salon news.
- Email campaigns are designed to drive repeat visits, promote special offers, and build a loyal customer base at minimal cost.
- All marketing emails comply with GDPR and include easy unsubscribe options.

## Search engine optimization

To improve search engine visibility and attract the right audience, the following SEO keywords are targeted throughout the site:

- Hair salon
- Book hair appointment online
- Buy hair products online
- Natural hair care
- Curly hair salon
- Hair treatments
- Salon near me
- Hair styling products
- Hair braiding services
- Hair salon reviews
- Best hair salon for curls
- Salon booking platform
- Hair care tips
- Hair product shop
  These keywords are used in page titles, meta descriptions, headings, and content to maximize organic search reach.

## Social media marketing

A facebook page was created to build community from the target market. Facebook is free and it also takes little to no time to set up and also it has so many users whom a business can strive to maintain a certain relationship, create content and connect with a target audience.

![facebook](static/images/facebook.jpg)

## Technologies

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

- [Javascript](https://www.javascript.com/)

- [Python](https://www.python.org/)

### Frameworks, programs and libraries used

- [Django](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

- [Github](https://github.com/) - I used Github to store all the data of my project after pushing it

- [Heroku](https://www.heroku.com/) - is a cloud platform service I used to deploy and host the project

- [ElephantSQL](https://www.elephantsql.com/) - used as a database for the project

- [Font Awesome](https://fontawesome.com/) - Was used to add icons for my social media links.

- [PEP8ci](https://pep8ci.herokuapp.com/) - I used it to validate python code

- [Balsamiq](https://balsamiq.com/) - was used to draw wireframes

- [dbdiagram](https://dbdiagram.io/home) - was used to draw the database schema

- [Stripe](https://stripe.com/en-ie) - was used for checkout functionality and facilitate online payments

- [Cloudinary](https://cloudinary.com) - for storage of assets

- [Freepik](https://freepik.com) - images used for the project

- [ChatGPT](https://www.chatgpt.com) - some images were generated by chatGPT

# Deployment

I developed this site on VS code, using git for version control. Then deployed to Heroku using the following steps

- Log in to [Heroku](https://id.heroku.com/login) or create an account

- Click New and Create New App

- I selected Europe as region.

- Click Create App button

- Add config var DATABASE-URL, and for the value, copy in your databse url from ElephantSQL. do not add quotation marks around your database

- Update requirements.txt: pip freeze > requirements

- import dj_database_url in settings and update your database

- migrate your database

- create a new superuser for your database and at this point your database is exposed do not commit it to github

- Install gunicorn and freeze into the requirements file

- Then create Procfile

- DISABLE_COLLECTSTATIC

- Commit and push to github

- On your app in Heroku go to Deploy and connect it to github and search your repository, click connect.

- Choose automatic or manual deploy. Click deploy branch

- When complete click View to open the deployed app

## From Github docs

### Forking

- Open GitHub page that hosts the repository you wish to fork.
- Find the 'Fork' button at the top right of the page
- Once you click the button the fork will be in your repository

### Cloning

- Open Go to the repository page on Github
- click on the green button that says "Code".
- You can choose to download a zip file of the repository, unpack it on your local machine, and open it in your IDE.
- Copy the URL under the HTTPS tab to clone using https.
- In a new window, and set the current directory to the one you want to contain the clone from.
- Type git clone and paste the URL copied from the GitHub page.
- The repository clone will now be created on your machine.

## Credits

- Code Institute Botique Ado walk through

- Hello django code institute

- [Dataflair django tutorial](https://data-flair.training/blogs/django-tutorials-home/)

- [Stack overflow](https://stackoverflow.com/)

### Acknowledgement and support

- Our cohort coordinator, Kay

- My Mentor, Jubril

- My classmates

- My friend, Anita, the owner of a hair salon that I took inspiration from
