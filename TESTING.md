# Testing Section - You Made You Fitness Community

Link back to README documentation **here**

Table of Contents

## Code Validators

### HTML

To validate the HTML code for all pages I used the **[W3C Markup Validation Service](https://validator.w3.org/nu/)**. Where necessary, the code was validated by direct input. The results are presented below.

<details>
<summary>Home App</summary>
<br>

home.html
![home page html validation](/documentation/testing/html-validation-home-page.png)
</details>

<details>
<summary>Community App</summary>
<br>

community_unauthorized.html
![community unauthorized user html validation](/documentation/testing/html-validation-community-unauthorized.png)

community.html
![community start html validation](/documentation/testing/html-validation-community-start.png)

recipe_post_page.html
![community recipe list html validation](/documentation/testing/html-validation-recipe-list.png)

workout_post_page.html
![community workout list html validation](/documentation/testing/html-validation-workout-list.png)

other_post_page.html
![community other post html validation](/documentation/testing/html-validation-other-post-list.png)

recipe_post_detail_page.html
![community recipe detail html validation](/documentation/testing/html-validation-recipe-detail.png)

workout_post_detail_page.html
![community workout detail html validation](/documentation/testing/html-validation-workout-detail.png)

other_post_detail_page.html
![community other post detail html validation](/documentation/testing/html-validation-other-detail.png)

add_recipe_post.html
![community add recipe html validation](/documentation/testing/html-validation-add-recipe.png)

add_workout_post.html
![community add workout html validation](/documentation/testing/html-validation-add-workout.png)

add_other_post.html
![community add other post html validation](/documentation/testing/html-validation-add-other-post.png)

edit_recipe_post.html
![community edit recipe html validation](/documentation/testing/html-validation-edit-recipe.png)

edit_workout_post.html
![community edit workout html validation](/documentation/testing/html-validation-edit-workout.png)

edit_other_post.html
![community edit other post html validation](/documentation/testing/html-validation-edit-other-post.png)

logged_in_user_posts.html
![logged in user posts html validation](/documentation/testing/html-validation-user-posts.png)

search_results.html
![community search result html validation](/documentation/testing/html-validation-search-result.png)

</details>

<details>
<summary>Products App</summary>
<br>

products.html
![product guide list html validation](/documentation/testing/html-validation-product-view.png)

product_guide_detail.html
![product detail view html validation](/documentation/testing/html-validation-product-detail.png)

</details>

<details>
<summary>Cart App</summary>
<br>

cart.html
![cart view html validation](/documentation/testing/html-validation-cart-view.png)

</details>

<details>
<summary>Checkout App</summary>
<br>

checkout.html
![checkout view html validation](/documentation/testing/html-validation-checkout-page.png)

checkout_success.html
![checkout success html validation](/documentation/testing/html-validation-checkout-success-page.png)
</details>

<details>
<summary>Contact App</summary>
<br>

contact.html
![contact page html validation](/documentation/testing/html-validation-contact-page.png)

</details>

<details>
<summary>Authentication</summary>
<br>

login.html
![login page html validation](/documentation/testing/html-validation-allauth-login.png)

logout.html
![logout page html validation](/documentation/testing/html-validation-allauth-logout.png)

signup.html
![signup page html validation](/documentation/testing/html-validation-allauth-signup.png)

I could not locate where to fix these warnings in the imported allauth templates, but will with more time look into it.

![signup page html validation warning](/documentation/testing/html-validation-allauth-signup-warnings.png)

</details>


### CSS

To validate the CSS code for this project I used the **[Jigsaw W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)**. The results are presented below.

![css validation](/documentation/testing/css-validation-ymy-heroku.png)

Before deploying the project I also used the same service to validate the additional css files presented below.

community.css
![css validation community](/documentation/testing/css-validation-additional-comminitycss.png)

checkout.css
![css validation checkout](/documentation/testing/css-validation-additional-checkoutcss.png)

### JavaScript

To validate the JavaScript code for this project I used **[JSHint](https://jshint.com/)**.

Base
![javascript message function test result](/documentation/testing/js-hint-base-message.png)

Checkout
![javascript checkout function test result](/documentation/testing/js-hint-checkout-stripe.png)

Cart
![javascript cart function test result](/documentation/testing/js-hint-cart-remove.png)

Community
![javascript community function test result](/documentation/testing/js-hint-community-slug.png)


### Python

To validate the Python code for this project, I used **[CI Python Linter](https://pep8ci.herokuapp.com/)** the . The results are presented below.

<details>
<summary>Home App</summary>
<br>

apps.py
![python testing of home apps.py](/documentation/testing/python-linter-home-appspy.png)

views.py
![python testing of home views.py](/documentation/testing/python-linter-home-viewspy.png)

urls.py
![python testing of home urls.py](/documentation/testing/python-linter-home-urlspy.png)
</details>

<details>
<summary>Community App</summary>
<br>

admin.py
![python testing of community admin.py](/documentation/testing/python-linter-community-adminpy.png)

apps.py
![python testing of community apps.py](/documentation/testing/python-linter-community-appspy.png)

forms.py
![python testing of community forms.py](/documentation/testing/python-linter-community-formspy.png)

models.py
![python testing of community models.py](/documentation/testing/python-linter-community-modelspy.png)

urls.py
![python testing of community urls.py](/documentation/testing/python-linter-community-urlspy.png)

views.py
![python testing of community views.py](/documentation/testing/python-linter-community-viewspy.png)

</details>

<details>
<summary>Products App</summary>
<br>

admin.py
![python testing of products admin.py](/documentation/testing/python-linter-products-adminpy.png)

apps.py
![python testing of products apps.py](/documentation/testing/python-linter-products-appspy.png)

models.py
![python testing of products models.py](/documentation/testing/python-linter-products-modelspy.png)

urls.py
![python testing of products urls.py](/documentation/testing/python-linter-products-urlspy.png)

views.py
![python testing of products views.py](/documentation/testing/python-linter-products-viewspy.png)

</details>

<details>
<summary>Cart App</summary>
<br>

apps.py
![python testing of cart apps.py](/documentation/testing/python-linter-cart-appspy.png)

contexts.py
![python testing of cart contexts.py](/documentation/testing/python-linter-cart-contextspy.png)

urls.py
![python testing of cart urls.py](/documentation/testing/python-linter-cart-urlspy.png)

views.py
![python testing of cart views.py](/documentation/testing/python-linter-cart-viewspy.png)

</details>

<details>
<summary>Checkout App</summary>
<br>

admin.py
![python testing of checkout admin.py](/documentation/testing/python-linter-checkout-adminpy.png)

apps.py
![python testing of checkout apps.py](/documentation/testing/python-linter-checkout-appspy.png)

forms.py
![python testing of checkout forms.py](/documentation/testing/python-linter-checkout-formspy.png)

models.py
![python testing of checkout models.py](/documentation/testing/python-linter-checkout-modelspy.png)

signals.py
![python testing of checkout signals.py](/documentation/testing/python-linter-checkout-signalspy.png)

urls.py
![python testing of checkout urls.py](/documentation/testing/python-linter-checkout-urlspy.png)

views.py
![python testing of checkout views.py](/documentation/testing/python-linter-checkout-viewspy.png)

</details>

<details>
<summary>Contact App</summary>
<br>

apps.py
![python testing of contact app.py](/documentation/testing/python-linter-contact-appspy.png)

urls.py
![python testing of contact urls.py](/documentation/testing/python-linter-contact-urlspy.png)

views.py
![python testing of contact views.py](/documentation/testing/python-linter-contact-viewspy.png)

</details>

<details>
<summary>YouMadeYouFitness Project</summary>
<br>

asgi.py
![python testing of project asgi.py](/documentation/testing/python-linter-project-asgipy.png)

settings.py
![python testing of project settings.py](/documentation/testing/python-linter-project-settingspy.png)

urls.py
![python testing of project urls.py](/documentation/testing/python-linter-project-urlspy.png)

wsgi.py
![python testing of project wsgi.py](/documentation/testing/python-linter-project-wsgipy.png)

</details>

## Accessibility

- Wave report goes here.

### Lighthouse Report

### Manual Testing

| TEST PASS | USER STORY | TEST | 
| --- | ----------- | ----------- |
|  | #1A Navigation Bar: As a site user, I can easily find the navigation bar, so that I can navigate the different pages of the site. | Given that a user visits the site, when exploring different pages, then the navbar is visible at the top of the screen at all times.   |
|  | #1B Business Logo: As a site user, I can relocate to the home page by clicking the business logo in the navbar, so that it is easily accessible when needed.  |  Given that a user visits the page, when the logo in the navbar is clicked, then the user will be relocated to the home page.  |
|  | #2A Home Page: As a site user, I can understand the purpose of the site simply by looking at the home page, so that I can decide if I want to explore the content further. |  Given that a first time user visits the site, when they land on the home page, then they know that it is a site for a fitness community.  |
|  | #2B Contact Information: As a site user, I can find the business contact information, so that I know how to get in touch with them.  |  Given that a user wants to get in touch, when they need to find the contact information, then they can find a link to the contact page in the navbar.  |
|  | #2C About Us Section: As a site user, I can find a section with information about the fitness community, so that I can learn more about it.  |  Given that a user visits the site, when looking for more information about the community, then they can find an about us section on the home page.  |
|  | #2D Web Shop: As a site user, I can open the web shop, so that I can scroll through the products the fitness community offer. |    |
|  | #2E Blog Page: As a registered user, I can view the blog page, so that I can take part of other member’s posts |  Given that a registered user is logged in, when wanting to read blog posts, then they can find a community page with all available blog posts.  |
|  | #2F Social Media Links: As a site user, I can find the fitness community’s social media links, so that I can learn more about their business. |  Given that a user is visiting the site, when looking for the fitness communitys social media, then they can find links in the footer on all pages.  |
|  | #2G Wish List: As a site user, I can add products to a wish list, so that I can save my favorites for later.  |    |
|  | #3A Create Account: As an unregistered user, I can create an account, so that I can make purchases and take part of blog posts.  |  Given that a user wants register, when clicking register/signup, then they can fill out a form with username and password and email (optional) to create an account.  |
|  | #3B Login: As a registered user, I can easily login to my account, so that I can access my profile and the content for registered users.  | Given that a user wants to log in, when entering their username and password, then the user will log in and be relocated to the specific view for logged in users.  |
|  | #3C Logout: As a registered user, I can easily logout from my account, so that I can protect my personal information |  Given that a logged in user wants to log out, when the logout button is clicked, then the user will be logged out and return to the home page.  |
|  | #3D Reset Password: As a registered user, I can reset my password, so that I can access my information and keep my account safe.  |    |
|  | #3E Update Profile: As a registered user, I can change my profile information, so that I can ensure it is up to date.  |    |
|  | #3F Delete Account: As a registered user, I can delete my account, so that I have the option to remove my information from the site.  |    |
|  | #4A View Products: As a site user, I can view the products in the web shop, so that I can decide if I want to make a purchase. |  Given that a user is interested in making a purchase, when looking in the webshop, then they can scroll through all the communitys available products.  |
|  | #4B Search for Products: As a site user, I can search for products by category or name, so that I can find what I am looking for.  |    |
|  | #4C Add to Shopping Cart: As a site user, I can add products to my shopping cart, so that I can prepare for making a purchase. |  Given that a user has decided to add something to their shopping cart, when they click an add to cart button, then the product is added to the shopping cart.  |
|  | #4D Edit Shopping Cart: As a site user, I can delete the products in my shopping cart, so that I can easily make changes if needed. |  Given that a user wants to update their shopping cart, when clicking the trash can next to an item, then the item is removed from the shopping cart. |
|  | #4E Checkout: As a registered user, I can fill out my contact and payment information, so that I can complete the purchase.  |  Given that a user wants to go through with their purchase, when clicking checkout, then they can fill out their information to complete the purchase.  |
|  | #5A Make Blog Post: As a registered user, I can make a blog post, so that I can share content with the community. |    |
|  | #5B Edit/Delete Blog Post: As a registered user, I can edit or delete my blog post, so that it is possible to make changes if needed. |  Given that a user wants to share a blog post, when clicking an add post button, then they can fill out a form to create their blog post.  |
|  | #5C Like Blog Post: As a registered user, I can like or unlike other user’s blog posts, so that I can interact with their content. |    |
|  | #5D Search for Blog Posts: As a registered user, I can search for blog posts using key words, so that I can find specific content. | Given that a user is looking for a specific blog post, when entering a word to the search bar, then the search results are displayed.   |
|  | #6A Add Products: As a site admin, I can add, edit, and delete products to/in/from the web shop, so that I can ensure it is up to date with the latest news. | Given that a site admin is logged in, when viewing the webshop from the the admin panel, then they can add, edit and delete products.   |
|  | #6B Manage Blog Posts: As a site admin, I can delete blog posts made by users, so that I can ensure that available content is appropriate and following community guidelines. |  Given that a site admin is logged in, when viewing the blog posts from the admin panel, then they can delete posts if they are not in line with the communitys guidelines.  |

| TEST PASS | TEST |
| ------- | -------- |
|  | Links and buttons take the user to its intended pages  |
|  | Social media links open in a new window  |
|  | The different sections of the site are responsive and work on different screen sizes  |
|  | There is a page where the user can show the blog posts they have made  |
|  | A 404 page is displayed when the user is trying to view a page that does not exist  |
|  | User feedback is displayed in the for of messages when actions are made  |
|  | The user is taken to a thank you page when completing a purchase  |

### Browsers

### Bugs

- I did not manage to create a view for deleting items from the shopping cart in views.py. Fixed by adding js code instead.

### Unsolved Bugs

Link back to README documentation **here**
