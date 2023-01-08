# Sneakerpoint
Sneaker marketplace for new and used sneakers.

Please visit the website [here](https://sneakerpoint.herokuapp.com/).

## Introduction and purpose

The Sneakerpoint e-commerce website has been developed as part of the Milestone project 5 for Code Institute Diploma in Software Development with eCommerce. The Sneakerpoint is an e-commerce applicationbuilt in Django, incorporating Python, CSS and HTML.

The application provides a fully functional solution for a e-commerce business selling new and used sneakers. Business owner and the admin of the application is able to manage products available throughout the website as well as users (Sneakpoint customers), orders and queries from customers.
The target audience of the site are users who look to purchase either new or used sneakers. Customers of Sneakerpoint are allowed to register and manage their user profiles as well as complete orders, including payment for the order.

![Multidevice view](webimages/multidevice.PNG)

## Design 

The below section of the document outlines development journey of the application starting from the concept to ultimate solution used to develop the site.

### 1 Concept

The concept of the project was to develop a fully functional e-commerce application, which would allow the business owner to run a business.
The business owner/site administrator is able to manage many of the functions via Django's admin portal however a functionality has been developed to allow site administrator to manage upload, edit and deletion of products via user interface. 
As for the target audience and ultimate users of the applications, are the customers interested in purchasing sneakers. In order to faciliate the process a customer profile can be created in order to retain key customer information such as address and contact details.

From a business point of view the desire was to develop an application, which would be user friendly, simple to use and browse the products as well as complete the purchase, using credit or debit cards.

### 2 Functional scope 

In terms of overall functional scope of the application the following key areas were needed to be developed in order for the site to operate as required:

**Site admin** - the primary means of managing the site from admin point of view is through a default admin portal supplied by Django's framework. With that said, the site admin is also allowed to manage products via user interface (Sneakerpoint site), whereby a product can be added, edited and deleted if necessary.

**Registration and Login**- site visitors and potential customers are invited to register via an option available in the navbar menu Customer Centre. The registration and login process is supported by Django's allauth solution. The registration process has been enhanced through email notifications, which users receive at the time of registration on the site.

**User Profile** - once registered customers can maintain and update their customer details, including address information. The profile also allows the users to view orders, which have been placed previously.

**Contact Us**- this functionality allows registered and unregistered site users to send queries to Sneakerpoint. The Contact Us is available through Customer Centre in the navbar and allows the users to submit query or a question they may have. Submissions are handled through a form available to users, and which requires user to provide their email address, subject and the actual message. Once the request is submitted users will receive confirmation that the query has been received. The actual queries are recorded in the database for site admin or the business owner to review and respond to client. The responses will need to be managed through an external email for now.

**Customer Reviews**- THIS FUNCTIONALITY IS PARTIALLY DEVELOPED - this functionality allows registered and logged in users to submit customer reviews. Once the user is logged in the user will be able to see their name and under the customer review will be logged under. Whilst at the moment the customer reviews are recorded in the database, the actual customer reviews are not yet displayed on the website that so these can be viewed by other, non logged users.

**Wishlist**- this functionality allows registered and logged users to add products to their personal wishlist. Any products in user's wishlist can be reviewed further by clicking details button or alternatively products can be removed from the list at a click of a button. The wishlist functionality tracks all the users who have created a wishlist. In addition wishlists also tracks the individual products, which form part of users' wishlists.

**Bag** - this functionality allows customers to add products to a bag, should they decide to proceed and complete the purchase. Each addition of a product will update the bag and also provide user with a notificaiton message. Within the bag the user may take actions to update the quantity of product or remove them from the bag. The bag also allows the users to proceed to checkout section, where the purchase can be completed.

**Checkout**- this part of functionality allows the users to complete the purchase of product/s they have selected. As part of the checkout process, the user will be required to provide their details such as name, email address and a shipping address. Users will also need to provide credit card details in order to complete the purchase.

**Card payments**- the application incorporates credit card payment solution provided by Stripe in order to complete payments. The solution allows to provide real time feedback to customers in event if the credit card payment is rejected or the card number is incorrect. There are mutliple events, which Stripe will provide detailed feedback on to a user if required.

**Newsletter**- registered and unregistered users are able to provide their email address and sign up for a free newsletter from the business.


### 3 Solution 

In order to develop the application, and given the functional needs the following solutions were used:

**Languages**

Given the fact that the nature of the application allows for a frequent content manipulation, a standard HTML solution would not work.
The solution needed to incorporate Python in order to make the solution more agile, in terms of development of relevant functions and in order for the user actions to be able to interact with the database in place. 
As part of the development the following languages were used:
- HTML
- CSS
- Python
- Javascript

**Database**

The application required a database structure, which would support managing various aspects of running the e-commerce business.
The key needs from databasr perspective were related to managing products, profiles/accounts, orders, customer queries, customer reviews and wishlist.
For the purpose of managing database related needs, Postgresql was selected as a solution for this project.

The below reflects database schema developed in order to support the needs of this project.

![database](webimages/database.PNG)

**Development**

For the purpose of development of this project a number of technologies were used. 

- GitHub repository was used to store the project's code after being pushed from Gitpod.
- Gitpod IDE was used for version control by utilizing the Gitpod terminal to commit and Push to GitHub.
- Django framework was used to develop structure of the application and also to use some of the already developed functions of Django such as user authorisation, admin portal and others.
- Bootstrap5 was used for construction of the application application and responsiveness.
- Crispy forms library 
- DrawSQL was used for drawing database schema.
- Balsamiq was used for creation of wireframes during the initial design process.
- Google Gmail for sending user emails.
- Heroku was used for hosting the application
- PostgreSQL was used to manage database of the application
- AWS was used for storing static files and product images.
- Mailchimp was used to manage collection of newsletter signups from users.

### 4 Wireframes 

In the the process of the application being designed the below wireframes have been drafted and put together.
Wireframes have been designed for both desktop and mobile views.

<details open>
<summary>Desktop</summary>
<br>

Homepage

![homepage](webimages/homepage.PNG)
 
Products
 
![products](webimages/productview.PNG)
 
Individual product details 
 
![product](webimages/individualproduct.PNG)
 
Sign up
 
![signup](webimages/signup.PNG)
 
Login
 
![login](webimages/login.PNG)
 
Logout
 
![logout](webimages/logout.PNG)
 
User Profile
 
![userprofile](webimages/userprofile.PNG)
 
Contact Us 
 
![contact](webimages/contact.PNG)

Wishlist 
 
![wishlist](webimages/wishlist.PNG)
 
Customer Review Submission 
 
![customerreviewsubmission](webimages/customerreviewsubmit.PNG)
 
Customer Reviews Summary 
 
![reviews](webimages/customerviewssummary.PNG)
 
Shopping Bag 
 
![shoppingbag](webimages/shoppingbag.PNG)
 
Checkout 
 
![checkout](webimages/checkout.PNG)
 
Product Management
 
![productmanagement](webimages/productmanagement.PNG)
 
 
</details>

<details open>
<summary>Mobile</summary>
<br>

 Homepage  

![homepage](webimages/mobilehomepage.PNG)
 
Products
 
![products](webimages/mobileproducts.PNG)
 
Individual product details 
 
![product](webimages/mobileindividualproduct.PNG)
 
Sign up
 
![signup](webimages/mobilesignup.PNG)
 
Login
 
![login](webimages/mobilelogin.PNG)
 
Logout
 
![logout](webimages/mobilelogout.PNG)
 
User Profile
 
![userprofile](webimages/mobileprofile.PNG)
 
Contact Us 
 
![contact](webimages/mobilecontact.PNG)

Wishlist 
 
![wishlist](webimages/mobilewishlist.PNG)
 
Customer Review Submission 
 
![customerreviewsubmission](webimages/mobilereviewsubmit.PNG)
 
Customer Reviews Summary 
 
![reviews](webimages/mobilereviewssummary.PNG)
 
Shopping Bag 
 
![shoppingbag](webimages/mobileshoppingbag.PNG)
 
Checkout 
 
![checkout](webimages/mobilecheckout.PNG)
 
Product Management
 
![productmanagement](webimages/mobileproductmanagement.PNG)
 
</details>

### 5 User Stories

The development of the project was based on User Stories created for the purpose of this project. The User stories were created and managed through a Kanban board available in GitHub. 
There were total of 19 User Stories which had been created for this development. The User Stories had been labelled accordingly to reflect 3 categories assigned such as: Must-Have, Should-Have and Could-Have. The progress in development was reflected in User Stories being moved from To Do, In Progress to Done section of the Kanban board. 

All of the User Stories for this project can be accessed [here](https://github.com/users/adamwasiak/projects/3/views/2).

### 6 E-commerce business model and marketing 

### Business model 

Sneakerpoint is a business to consumer e-commerce website offering its users (consumers) a platform to purchase sneakers, new and used. Consumers who wish to proceed with a purchase will be required to register and such users will avail of site functionality to store their shipping information and also details of previous orders.
Consumers who are visiting the site for the very first time are not required to register and can browse and access all information about the products across the Sneakerpoint site.As a modern day e-commerce site, Sneakerpoint allows users to purchase their prouducts using payment cards as a main and the only method of payment for now.
At the present, the business concept is limited to business to consumer model, whereas with time and site expansion the model could also include consumer to consumer. The latter would allow site users to offer their products (sneakers) to other consumers. The Sneakerpoint as a business, in such scenario would commercially benefit by applying a fee to each transaction.

### Marketing

The following marketing have been used in order to promote the business:

**SEO** - search engine optimazation has been also used including use of meta data in html structure, targeting the page word content with potential search on the web.
In addition robots.txt file and sitemap.xml have been both added to the structure of the application for enhanced search optimazation.

**Facebook business page** - a business page has been created on Facebook in order to increase engagement and outreach to potential customers. Facebook page will offer the business a direct engagement with potential customers and sneakers lovers across the globe.

![facebookpage](webimages/Facebookpage.PNG)

**Newsletter** - Mailchmip has been used and linked to the application for the purpose of getting users and potential customers to sign up for business updates and promotions.

## User Experience

The Sneakerpoint e-commerce site has been developed with an aim to make the user experience pleasant, intuitive and simple in terms of site navigation.
The key objective was to make the site visually appealing for users through a combination of a balanced ratio between good sized images and essential use of text and buttons.

The below Features sections illustrates all the key features currently available to Sneakerpoint users.

## Features 

SECTION CONTENT TO BE ADDED

## Future developments

SECTION CONTENT TO BE ADDED

## Testing 

There has been an extensive testing completed prior to final deployment. The 2 key areas of testing were related to functional and code validation.

**Functional**

The functional testing has been completed manually and the test scenarios and the test results have been captured in the documents below. The document break the test scripts into a number of functional test groups. Overall testing has been successful, with only 1 aspect being identified as an issue. The issue has been noted in the unfixed bugs section below.

![tests1](webimages/tests1.PNG)

![test2](webimages/test2.PNG)

**Code validation testing**

SECTION CONTENT TO BE ADDED

**HTML code validation**

SECTION CONTENT TO BE ADDED

**Python code validation**

SECTION CONTENT TO BE ADDED

**CSS code validation**

SECTION CONTENT TO BE ADDED

**Lighthouse – Dev Tools**

SECTION CONTENT TO BE ADDED

*Desktop*

SECTION CONTENT TO BE ADDED

*Mobile* 

SECTION CONTENT TO BE ADDED

**Bugs**

SECTION CONTENT TO BE ADDED

 **Fixed Bugs**
 
 SECTION CONTENT TO BE ADDED
  
 **Unfixed Bugs**

SECTION CONTENT TO BE ADDED
 
## Deployment 

The application was deployed in Heroku. In addition a bucket was setup in AWS in order to store static files and media images.

SECTION ABOVE TO BE EXPANDED WITH MORE DETAILED STEPS OF THE ACTUAL DEPLOYMENT PROCESS


## Project status as of 27th November

Due to timecontraints the project is deemed to be partially complete. The following elements still need to be worked on:

**1** - 1 additional model (Customer reviews) requires further development and completion. 

**2** - resposive design for some of the pages of the application requires to be reviewed in more detail in order to improve user experience.

**3** - although good level of testing has been completed a more complete revision of test scenarios is still required. Documentation to be added to Readme document.

**4**- Readme document has a number of gaps, which have not been completed yet due to time constraints to complete the project.

**5**- a thorough code review is still required in order to ensure that the code is structed in line with industry practices, including inclusion of additional comments.

**6**- user stories success criteria require to be updated with more detailed descriptions.

**7**- description of the e-commerce business model in the Readme document.


## Credits

- The thyme of the application is influenced by Code Institute's walkthrough project Boutique Ado
- Products and frontpage images were acquired from unsplash.com
- Thank you to my mentor Daisy for continuous support and guidance.

