# You Made You Fitness Community

The live application can be found here: **[You Made You Fitness Community](https://you-made-you-fitness-e606c79e6b9a.herokuapp.com/)**

![screenshot of amiresponsive](/documentation/images/amiresponsive-ymyfitness.png)

## Table Of Contents
- [You Made You Fitness Community](#you-made-you-fitness-community)
  - [Table Of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [User Experience(UX)](#user-experienceux)
    - [Epics and User Stories](#epics-and-user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
  - [Business Model](#business-model)
  - [Data Model](#data-model)
  - [Web Marketing](#web-marketing)
    - [Facebook Business Page (Social Media Marketing)](#facebook-business-page-social-media-marketing)
    - [Search Engine Optimization (SEO)](#search-engine-optimization-seo)
    - [Newsletter Signup (Email Marketing)](#newsletter-signup-email-marketing)
  - [Agile Methodology](#agile-methodology)
  - [Features](#features)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)

## Introduction

You Made You Fitness Community is an online e-commerce application that sells digital workout guides. The goal of the site is to offer a place of inspiration, support and fellowship for those interested in fitness and health on all levels. Users can sign up to take part of and share blog posts while the workout guides are available to purchase for everyone.

This project was created using HTML, CSS, JavaScript, Python, and Django, and is my 5th and final Portfolio Project for Code Institute's Diploma in Full Stack Software Development.

## User Experience(UX)

### Epics and User Stories

| Epic | ID | User Story |
| --- | ----------- | ----------- |
| Navigation |     |     |
|  | #1A | Navigation Bar: As a site user, I can easily find the navigation bar, so that I can navigate the different pages of the site. |
|  | #1B  | Business Logo: As a site user, I can relocate to the home page by clicking the business logo in the navbar, so that it is easily accessible when needed.  |
| Content |     |     |
|  | #2A  | Home Page: As a site user, I can understand the purpose of the site simply by looking at the home page, so that I can decide if I want to explore the content further. |
|  | #2B  | Contact Information: As a site user, I can find the business contact information, so that I know how to get in touch with them.  |
|  | #2C  | About Us Section: As a site user, I can find a section with information about the fitness community, so that I can learn more about it.  |
|  | #2D  | Web Shop: As a site user, I can open the web shop, so that I can scroll through the products the fitness community offer. |
|  | #2E  | Blog Page: As a registered user, I can view the blog page, so that I can take part of other member’s posts |
|  | #2F  | Social Media Links: As a site user, I can find the fitness community’s social media links, so that I can learn more about their business. |
|  | #2G  | Wish List: As a site user, I can add products to a wish list, so that I can save my favorites for later. |
| Registration and Account Management |     |     |
|  | #3A  | Create Account: As an unregistered user, I can create an account, so that I can take part of blog posts.  |
|  | #3B  | 3B. Login: As a registered user, I can easily login to my account, so that I can access the content for registered users.  |
|  | #3C  | Logout: As a registered user, I can easily logout from my account, so that I can protect my personal information |
|  | #3D  | Reset Password: As a registered user, I can reset my password, so that I can access my information and keep my account safe.  |
|  | #3E  | Update Profile: As a registered user, I can change my profile information, so that I can ensure it is up to date.  |
|  | #3F  | Delete Account: As a registered user, I can delete my account, so that I have the option to remove my information from the site.  |
| Web Shop |     |     |
|  | #4A  | View Products: As a site user, I can view the products in the web shop, so that I can decide if I want to make a purchase. |
|  | #4B  | Search for Products: As a site user, I can search for products by category or name, so that I can find what I am looking for.  |
|  | #4C  | Add to Shopping Cart: As a site user, I can add products to my shopping cart, so that I can prepare for making a purchase. |
|  | #4D  | Edit Shopping Cart: As a site user, I can delete the products in my shopping cart, so that I can easily make changes if needed. |
|  | #4E  | Checkout: As a site user, I can fill out my contact and payment information, so that I can complete the purchase.  |
| Blog Posts |     |     |
|  | #5A  | Make Blog Post: As a registered user, I can make a blog post, so that I can share content with the community. |
|  | #5B  | Edit/Delete Blog Post: As a registered user, I can edit or delete my blog post, so that it is possible to make changes if needed. |
|  | #5C  | Like Blog Post: As a registered user, I can like or unlike other user’s blog posts, so that I can interact with their content. |
|  | #5D  | Search for Blog Posts: As a registered user, I can search for blog posts using key words, so that I can find specific content. |
| Admin |     |     |
|  | #6A  | Add Products: As a site admin, I can add, edit, and delete products to/in/from the web shop, so that I can ensure it is up to date with the latest news. |
|  | #6B  | Manage Blog Posts: As a site admin, I can delete blog posts made by users, so that I can ensure that available content is appropriate and following community guidelines. |


### Strategy

**Project Goals:**

* The goal is to create an online fitness community that inspires and helps people take control over their own fitness journey. The name "You Made You Fitness Community" is meant to reflec this.

* The community will initially offer workout guides for all levels of fitness, but more products could be added in the future. Quality is key and all plans have to be proven to work. The community site needs to reflect a business that values high quality.

* The target audicence is people who are looking for tools to take charge of their fitness journey while also sharing the experience with a community. Previous fitness level does not matter as different plans for different goals are offered. Everyone is welcome.

**User Expectations:**

* Accessibility for all users.
* Easy navigation throughout the site.
* The purpose of the site is clear.
* A webshop where the products are relevant, clearly displayed and easy to browse through.
* A simple and safe checkout process.
* A visually pleasing design with pleasing color contrasts.


### Scope

**Contet Requirements and Functional Specification:**

* Authentication: Functionality to register and manage an account. 
* Web Shop: Functionality to complete a purchase.
* Products: Images and descriptions.
* Community Blog Page: For users to read and share blog posts.
* Functional Design: Responsiveness throughout the site.


### Structure

**Pages:**

Pages marked with ** are the same for unregistered and registered users.

**View for Unregistered Users:**

* Home Page**: Contains a hero image with text, in addition to sections with information and buttons linking to the most important pages of the site.

* Community Page: Contains links to login and signup for unregistered users.

* Webshop Page**: Page for all products in the webshop.

* Product Detail Page**: Contains product image, product details and add to cart button.

- Shopping Cart**: A view for products added to the shopping cart.

* Checkout Page**: Contains an order summary and form for user to fill out to complete a purchase.

* Checkout Success Page**: Displays an order summary when a purchase is successful.

* Sign In Page: Contains a log in form. 

* Sign Up Page: Contains a sign up form.

* Contact Page**: Contains contact information and newsletter signup.

**View for Registered Users:**

* Home Page**: Contains a hero image with text, in addition to sections with information and buttons linking to the most important pages of the site.

* Community Pages (blog): Built by different pages related to the site's blog functionality. Contains pages for viewing, adding, editing and deleting blog posts within each category.

* Webshop Page**: Page for all products in the webshop.

* Product Detail Page**: Contains product image, product details and add to cart button.

* Shopping Cart**: A view for products added to the shopping cart. 

* Checkout Page**: Contains an order summary and form for user to fill out to complete a purchase.

* Checkout Success Page**: Displays an order summary when a purchase is successful.

* Logout Page: Contains button for logging out.

* Contact Page**: Contains contact information and newsletter signup.

**Additional Pages:**

- 404 Page: Contains "page not found" message and link back to home page.

**Elements of Navigation:**

* A navigation bar with icons and links to its relevant content is visible at all times while navigating through the site.

* The business logo in the navigation bar is linked to the home page.

* The home page contains links to the most important content of the site.

* The footer contains links to relevant social media sites.

### Skeleton

<h4>Wireframes</h4>

Wireframes were created using **[Balsamiq](https://balsamiq.com/)**.

<details>
<summary>Home</summary>
<br>

![screenshot of home page wireframe](/documentation/images/wireframe-home.png)

</details>

<details>
<summary>Community</summary>
<br>

![screenshot of community wireframe for unauthorized users](/documentation/images/wireframe-commnity-unauthorized.png)

![screenshot of start page community wireframe for authorized users](/documentation/images/wireframe-community-authorized.png)

![screenshot of community post page wireframe](/documentation/images/wireframe-community-posts.png)

</details>

<details>
<summary>Products</summary>
<br>

![screenshot of products page wireframe](/documentation/images/wireframe-products.png)

![screenshot of products detail wireframe](/documentation/images/wireframe-product-detail.png)

</details>

<details>
<summary>Shopping Cart</summary>
<br>

![screenshot of shopping cart wireframe](/documentation/images/wireframe-shopping-cart.png)

</details>

<details>
<summary>Checkout</summary>
<br>

![screenshot of checkout wireframe](/documentation/images/wireframe-checkout.png)

</details>

<details>
<summary>Contact</summary>
<br>

![screenshot of contact page wireframe](/documentation/images/wireframe-contact.png)

</details>

### Surface

**Color Scheme**

The color scheme was created using **[Coolors](https://coolors.co/)** and follows a pink scheme that matches the hero image.

![screenshot of color scheme](/documentation/images/color-scheme.png)

## Business Model

![screenshot of business model](/documentation/images/BusinessModel-YMYFitness.png)

* To create the business model for this project I used **[creately](https://creately.com/)**.

* For tables of data and database planning, see the **[data model](#data-model)** section below.

## Data Model

ERD for models related to the Webshop functionality:
![sceenshot of ERD for webshop](/documentation/images/ERD-webshop.png)

ERD for models related to the Community blog posts:
![screenshot of ERD for the community app](/documentation/images/ERD-community.png)

* To create the entity relationship diagrams (ERD) for this project I used **[creately](https://creately.com/)**.

* The Webshop models were taken from Code Institute's walkthrough "Boutique Ado" and customized to fit an online business with digital products only.

* The Community blog post models (Recipe, Workout and OtherPost) were created by me to fit each category.

* The User model was provided by Django for a one to many relationship to the blog post models. Find more information about Django's default user model in the Django documentation **[here](https://docs.djangoproject.com/en/3.2/ref/contrib/auth/)**.

* In the future, it would be beneficial to create a one to many relationship between the User model and webshop functionality models, so that a registered user can autofill their checkout information and view their order history. The webshop checkout process is the same for both unregistered and registered users at the moment.

* A UserProfile model was created as the idea was to give users the ability to view both their own and other members profiles (in addition to editing their own). However, this functionality is yet to be implemented on the site due to lack of time before the submission date. Will be implemented in the future.

* This project uses a PostgreSQL database via **[ElephantSQL](https://www.elephantsql.com/)**.

## Web Marketing

### Facebook Business Page (Social Media Marketing)

A Facebook business page was created for You Made You Fitness Community.

![screenshot of facebook business page](/documentation/images/facebook-business-page-1.png)

![screenshot of facebook business page 2](/documentation/images/facebook-business-page-2.png)

Organic social media marketing would be a priority for further web marketing of this business. The interaction with users, free workouts, recipes and tips, competitions, offers on workout guides, and even in person events could all be beneficial marketing strategies for this type of business.

### Search Engine Optimization (SEO)

For this project, implemantations have been made from a Search Engine Optimization (SEO) perspective in order to ensure that potential customers can find "You Made You Fitness Community". The process is documented below.

**Keyword Research:**

1. Pen and paper were used to brainstorm general topics and possible keywords.
![screenshot of keyword brainstorm](/documentation/images/SEO-keywords-brainstorm.png)

2. A Google search was made for each keyword and the relevant results were documented in tables. Some of the keywords from the brainstorming were deleted/modified as they were too general.

![google search result presented in table](/documentation/images/SEO-google-search-1.png)
![google search result presented in table](/documentation/images/SEO-google-search-2.png)
![google search result presented in table](/documentation/images/SEO-google-search-3.png)

3. A mix of 10 short and long-tail keywords were selected based on the Google search results.

4. The relevance and authoritativeness was checked for some keywords using **[wordtracker](https://www.wordtracker.com/)** (I checked as many as I could before running out of free searches).

### Newsletter Signup (Email Marketing)

As part of a marketing strategy, the users can sign up to the community's monthly newsletter.
(As this is a fictional business the user can sign up, but no actual emails will be sent).

![screenshot of newsletter signup](/documentation/images/contact.png)

## Agile Methodology

This project was planned and created by the use of an agile approach. A GitHub project including issues (user stories), milestones and MoSCoW labels was created to keep track of the development process and progress.

View the GitHub project **[here](https://github.com/users/gustafsson96/projects/7/views/1)**.

**GitHub Project Board**

Issues were moved between Todo, In Progress, and Done as the work progressed. All items left in the "Todo" column when the project is submitted are labeled "won't have" for this release.

![screenshot of github project board](/documentation/images/github-project-board.png)

**Epics**

The epics were created as GitHub milestones. The user stories for each epic were then linked to its relevant milestone.

An additional milestone was included to keep track of the project set up. It only contains steps for setting up the project, no user stories.

![screenshot of github milestones](/documentation/images/github-milestones.png)

**User Stories**

The user stories were created as GitHub issues and contain related acceptance criterias and tasks (with the exepction of a few labeled "won't have" for this release). These were checked off continuously as the requirements were met.

![screenshot of github issues](/documentation/images/github-issues.png)


**MoSCoW Labels**

MoSCoW labels were created to prioritize the GitHub issues with user stories. An additional setup label for the intial setup steps was also included. I also kept the default documentations label, but ended up not using it.

![screenshot of labels](/documentation/images/github-labels.png)

## Features

<h3>Navigation Bar</h3>

The navigation bar for unauthorized users contains 7 nav items: Home, Community (view for unauthorized users), Webshop, Login, Join Us, Contact and Shopping Cart. The shopping cart amount is updated when product is added/deleted from the cart.

![screenshot of navbar unauthorized user](/documentation/images/navbar-unauthorized-user.png)

The navigation bar for authorized users contains 6 nav items: Home, Community (view for authorized users), Webshop, Contact, Logout, and Shopping Cart. The shopping cart amount is updated when product is added/deleted from the cart.

![screenshot of navbar authorized user](/documentation/images/navbar-authorized-user.png)

<h3>Home Page</h3>

The home landing page contains a hero image with a text box containing the business name and a button linking to the sign up page (for unauthorized users) or the community page (for authorized, logged in users).

![screenshot of hero container](/documentation/images/home-page-hero.png)

Below the home page, there are three sections. The "About Us" section contains more information about the business (and this could be improved further in the future). The "Need Some Guidance" section links to the webshop and is avaliable for both registered and unregistered user. The "Share Your Favorites" section links to the community page for either unregistered and registered users depending on if they are logged in or not.

![screenshot of home page content](/documentation/images/home-page-content.png)

<h3>Authentication</h3>

The register page (sign up) is where the user can create an account to join the community. It contains a form where username and password are required in order to sign up. Email is optional. There is also a link to the sign in page in case the user is already registered.

![screenshot of signup](/documentation/images/signup.png)

The login page contains a form where the user is required to fill out username and password in order to log in. There is also a link to the sign up page in case the user is not registered yet.

![screenshot of signin](/documentation/images/signin.png)

If the user clicks the "logout" navbar item they will relocate to the logout page. On the log out page they are asked if they are sure they want to log out. If the answer is yes, they can click the button to log out.

![screenshot of logout](/documentation/images/logout.png)

<h3>Webshop</h3>

In the webshop the products are evenly displayed with a product image, title and price. The user can click the image to get to the product detail page with more information and an "add to cart" button. The webshop is available for both unregistered and registered users.

![screenshot of webshop overview](/documentation/images/webshop.png)

The product detail page consists of the product image, title, description and price. The user can click "add to cart" if they want to purchase an item and "keep shopping" to go back to the webshop.

![screenshot of product detail page](/documentation/images/product-detail.png)

<h3>Shopping Cart</h3>

If there are items in the shopping cart, an overview of what is in the cart is displayed together with the cart total (the "bag" has been changed to "cart" since the screenshot was taken to keep it consitent). If the user wants to delete an item from the cart they can click the trash can icon. In addition to the order overview there are two buttons: one linking back to the webshop and one linking to the checkout page.

![screenshot of cart with items](/documentation/images/cart-items.png)

If there are no items in the shopping cart, a "your cart is empty" message is displayed together with a button linking back to the webshop.

![screenshot of empty cart](/documentation/images/cart-empty.png)

<h3>Checkout</h3>

The checkout page is where the user completes a purchase. An order summary is displayed and the user is prompted to fill out their information to complete the purchase. Since there are no physical products available (digital only) the user does not have to fill out their address. Name, number, email and card information is enough.

![screenshot of checkout view](/documentation/images/checkout-view.png)

When an order has been completed, a checkout success page is displayed with an order summary. 

![screenshot of checkout success page](/documentation/images/checkout-success.png)

<h3>Community</h3>

The community page for an unregistered user links to login and signup.

![screenshot of community page unauthorized users](/documentation/images/community-unauthorized.png)

For a registered user, the community page links to three sections: read posts, add posts, and the posts specific to the logged in user. For reading and adding there are three categories available: recipes, workouts and other posts. There is also a search bar available.

![screenshot of community start page](/documentation/images/community-start-page.png)

If the user clicks on one of buttons under "read other memebers posts" they are relocated to a post overview specific for the category they picked. The posts are displayed evenly with a default image, a title, author and "created on" date. The user can click on a title to read the post. In addition, there are two buttons available: one to add a post and one to go back to the community start page.

![screenshot of community post list](/documentation/images/community-post-list.png)

The post detail page contains the actual blog post and a button linking back to the post overview page.

![screenshot of post detail page](/documentation/images/community-post-details.png)

Under "your blog posts" the posts specific to the logged in user are displayed. The main CRUD functionality is available on this page as the user can edit and/or delete their posts. If there are no posts in a category a "there are no posts" message is displayed. 

![screenshot of logged in user posts](/documentation/images/community-user-posts.png)

The form for adding a post consists of different fields depending on category. The form presented below is for creating a general blog post.

![screenshot of adding a post](/documentation/images/community-add-post.png)

The form for editing a post looks similar to the "add a post" form, but is prepopulated with the content of the post that is getting edited.

![screenshot of editing a post](/documentation/images/community-edit-post.png)

The search results page displayed the search results for each category.

![screenshot of search results page](/documentation/images/community-search-result.png)

<h3>Contact</h3>

On the contact page the user can find the business email address. They can also sign up to the fitness community's newsletter (section created using mailchimp).

![screenshot of contact page](/documentation/images/contact.png)

<h3>Footer</h3>

The footer sticks to the bottom of the site on all pages and contains links to different social medias. 

![screenshot of footer](/documentation/images/footer.png)

<h3>Messages</h3>

When a user perfoms an action on the site, a message is displayed at the top of the screen. The messages disappear by themselves but the user can click the X if they want it to disappear faster. A few message examples are presented below.

![screenshot of a bootstrap message](/documentation/images/bootstrap-message-1.png)

![screenshot of a bootstrap message](/documentation/images/bootstrap-message-3.png)

![screenshot of a bootstrap message](/documentation/images/bootstrap-message-4.png)

![screenshot of a bootstrap message](/documentation/images/bootstrap-message-2.png)

<h3>Admin Panel</h3>

An admin can from the admin panel:

* Add, edit and delete products.
* Add, edit and delete blog posts. 
* View orders.

![screenshot of admin panel](/documentation/images/admin-panel.png)

<h4>Features Left to Implement</h4>

* Webshop: Additional add to cart button on products overview page.

* Community: Liking and commenting blog posts for a more interactive community experience.

* Updated Post: "Updated on" date and time for an updated post (included in the model but not the view).

* User Profile: Viewing other members user profiles with a potential profile picture and a bio (in addition to editing your own).

* Site Pagination: Site pagination should be implemented on the products and blog posts pages.

## Testing

Find the complete documentation for testing here: **[TESTING.md](TESTING.md)**

The testing documentation contains validation of HTML, CSS, Python, and JavaScript, Lighthouse Reports, accessibility testing, and manual testing.

## Deployment

<h4>Create a Repository</h4>

* Go to the **[ci-full-template](https://github.com/Code-Institute-Org/ci-full-template)**.
* Click "Use this template" and pick "Create a new repository".
* Add a name for your repository.
* Click the green "Create repository" button.
* Create a workspace for the new repository. I used Codeanywhere.

<h4>Install Django and Supporting Libraries</h4>

* Open up the workspace.
* Install Django: in the terminal, type "pip3 install 'django<4' gunicorn".
* Library for PostgreSQL: in the terminal, type: "pip3 install dj_database_url==0.5.0 psycopg2".
* Library for Cloudinary: in the terminal, type: "pip3 install dj3-cloudinary-storage".
* Make sure to create a requirements.txt file by using the command: "pip3 freeze --local > requirements.txt".
* Create a django project and django app. Make sure to add the app to the projects settings.py file.
* Create a Procfile and add in "web: gunicorn yourappname.wshi".

<h4>Create the Heroku App</h4>

* Log in/Sign up to **[Heroku](https://id.heroku.com/login)**.
* On the dashboard, click the "new" button and pick "Create new app".
* Name your app (must be a unique name) and select the region that is closest to you.
* Click the purple "Create app" button.

<h4>Cloudinary</h4>

* Log in/Sign up to **[Cloudinary](https://cloudinary.com/)**.
* Copy the API Environment variable on the dashboard.
* Add the copied variable to the env.py file.
* Make sure cloudinary is linked to the app in settings.py.

<h4>Create a Database (using ElephantSQL)</h4>

* Log in/Sign up to **[https://www.elephantsql.com/](ElephantSQL)**.
* On your dashboard, click "Create New Instance".
* Select a name and a plan (Tiny Turtle Free) and leave the Tags field blank.
* Click the green "Select Region" button.
* Pick a data center near you.
* Click the green "Review" button.
* Check your details before clicking the green "Create instance" button.
* Go back to the dashboard and click on the database instance name for this project.
* Copy the database URL displayed in the URL section.

<h4>env.py</h4>

* Make sure an env.py is created and added to the .gitignore file.
* In the env.py file, add "import os", a blank line, and then "os.environ["DATABASE_URL"]=copiedURL".
* Replace "copiedURL" with the string copied from ElephantSQL.
* Below the DATABASE_URL line, add "os.environ["SECRET_KEY"]="asecretkey".
* Replace "asecretkey" with a secret key of your choice (inside quotation marks).
* Add a variable called "os.environ["CLOUDINARY_URL"]". This is where the copied variable from cloudinary is added as value.
* Make sure to delete "CLOUDINARY_URL=" from the copied variable before saving.
* Add variables for stripe secret and public keys.

<h4>settings.py</h4>

* In the settings.py file for your Django project, add the following code: screenshot of code in settingspy
![screenshot of settings.py](/documentation/images/settingspy.png)

* Further down, change the SECRET_KEY variable by replacing the insecure Django key inside the quotation marks with "SECRET_KEY". This will reference the secret key created in the env.py file.
* Scroll down to the database section and comment out the default DATABASES variable.
* Instead, create a new DATABASES variable and give it the value " 'default': dj_database_url.parse(os.environ.get("DATABASE_URL")) " inside curly brackets.
* Add the Heroku host name to an ALLOWED_HOSTS variable.

<h4>Deploy to Heroku</h4>

* Remember to set debug to "False" in the apps settings.py file.
* Go to the Heroku dashboard and click on the project.
* Make sure Config Vars DATABASE_URL, SECRET_KEY, CLOUDINARY_URL, PORT and Stripe variables are present.
* Go to the "Deploy" section.
* Select GitHub as deployment method and connect your account.
* Search for your project's repository and click "Connect".
* Scroll down to the bottom of the page, and by "Manual deploy", make sure "main" is selected in the dropdown menu, and click "Deploy Branch".
* When the app has been deployed successfully, scroll to the top of the page and click "Open app" to view it.

<h4>Forking</h4>

* Log in to GitHub, search for the reopsitory name, and navigate to its main page.
* Locate the "Fork" button and click it.
* Add a description (optional).
* Click the green "Create fork" button.

<h4>Cloning</h4>

* Log in to GitHub and search for the repository name and navigate to its main page.
* Click the green "<> Code" button.
* Copy the URL (if using HTTPS, SSH and GitHub CLI are also available options).
* Open the terminal in your IDE and change the location to where you want the cloned repository.
* Type "git clone" followed by the copied URL from the GitHub repo.
* Press enter.

## Credits

<h3>Content</h3>

* All functionality required for a user to complete a purchase (Stripe included) has been copied from the Code Institue's walkthrough "Boutique Ado" videos.

* The Code Institue walkthrough "I Think Therefore I Blog" was helpful when creating the Community blog functionality.

* To better understand and implement search bar functionality I read **[this LearnDjango article](https://learndjango.com/tutorials/django-search-tutorial)** in addition to the Code Institue's walkthrough "Boutique Ado" videos.

* I used **[this StudyGyaan article](https://studygyaan.com/django/django-custom-404-error-template-page?utm_content=cmp-true&expand_article=1)** as a guide to create a 404 page.

* The sitemap was created using **[XML Sitemaps](https://www.xml-sitemaps.com/)**.

* I used the deployment steps from my 4th portfolio project ["The Swede Restaurant"](https://github.com/gustafsson96/the-swede-restaurant) as a guide when creating this project. 

* In addition to the more specific credits, I want to credit the Django Documentation, Stack Overflow, and the CI community on Slack as they have been helpful in solving problems along the way.

<h3>Media</h3>

* I used **[Adobe Express](https://new.express.adobe.com/)** to design the covers for the workout guides.

* The default post images were taken from **[Pexels](https://www.pexels.com/)**.

* The hero image was taken from **[Unsplash](https://unsplash.com/)**.
