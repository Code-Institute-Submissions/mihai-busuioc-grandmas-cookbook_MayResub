![Cookbook Logo](https://res.cloudinary.com/fr3shf4iry/image/upload/v1611168574/cook-sml_nq2nzr.png)

# Grandma's Cookbook

## Introduction

Experience Grandma's Cookbook, a easy to use recipe website, giving everyone access to their favorites just a few clicks away. 
A safe and responsive website to provide you with the tools needed to try out your old favorite recipe.  Add your own and share the love.


# UX


This website have been designed to give any visitors easy access to all of it's content without needing to signup,
 but provides the opportunity to register and contribute with their favorite recipe for the other fellow members.
  With the built in administrator portal, allowing for easy management  process for each recipe.
Making all content available to the visitor upon accessing the page. 


## Traversing
Key design decision allowing visitors, users, and administrator to access the entire page, and all CRUD functionality 
(Create, Read, Update and Delete) within as few clicks as possible, yet get to experience the entire platform for ease
of use.

## Smart Search
Built in Search comodity to manage the content on the website , allowing content to be found by searching for key ingredient,
 providing the visitor a quick overview and an easy to use website.


## User Stories

- Everyone at work loved my grandma's chocolate cake and asked for the recipe.

- Want to use it as my own digital recipe book for easy sharing.

- Sharing my favorite recipe with co-workers, family and friends.

- Quick access to recipes for cooking that is easy to follow.

- Want to add my own recipe to help others cook my recipes.

- A family member added a recipe they want to share.

- Want to try a receipe from a friend.


----------------------------------------------------------------------------

# Design Decisions
The design follows a minimalistic approach by only displaying content that is of value to the visitor, 
and keeping any overflow out of the design process, and relying heavily on dynamic user content. 
The Grandma's Cookbook takes much inspiration from the project Task-Manager from Coding Institute
Grandma's Cookbook uses light vintage like  colors, to have a clear contrast with the websyte vintage theme  to enhance 
overall visibility, and minimizing bombarding the visitors with colors, but rather finding the appropriate places to apply them.

## Typography
I choose to use Curseve  for the text  due to it's vintage looks and give the page a bit more personality  also not too vintage
 ( like Yesteryear) to help with readability.

-------

# Database
This website have 2 databases, 1 for users and 1 for recipes, these are both being used to connect with each other as
 well being used to store various calculations, and store all general information on the page. All the content on the page is 
 generated from these 2 databases.


# Features
All the features were developed with dynamic user content with appropriate restrictions. Features like create, update, delete, 
 are hidden behind a registration wall or login portal, but this do not hinder visitors from viewing the overall content.

## Home Page (visitor)
The home page includes Log In and Registration menu at the very top, where all the highest rated recipes comes into view with the 
option to search recipes by indredient or name. 

## Home Page (Registered/logged in)
After logging in a few new features appear, the header will now show Logout and your username and Add recipe 

## Home Page ( common )
Visitors, Registered users and administrator can see all the recipes in a accordeon style that expands to show the ingredients, 
number of portions and the author, click on the "Cook" button opens a modal with the instructions to cook the recipe.


## Administrator Profile (logged in)
This page allows you to see every recipe and a new link to "Manage Recipes" for quick edit or delete. 


## Add Recipe (Only available when logged in)
This can be found as a menu link once logged in on the home page.
Allowing the user to add their own recipe name, description text, portions, ingredients and the steps to make a recipe.
This page looks the same for user and administrator

## Edit Recipe (Only available when logged in and author of the recipe or admin inside the recipe accordeon )
Provides identical user interface as add recipe, but pulls all the data from the database to be edited 

## Features I want to implement
In time of development, I noticed multiple important features that should be added for the complete experience,
 but they are not necessary for the project to be completed and was left to be implemented later because of time constraints.
  Will be added after submision and grading:
 - pictures on recipes 
 - email on registeration
 - confirm password field on registration
 - popup modal to confirm deletion of recipes

# Technologies
## Languages

- HTML:	Creating the entire foundation for the website.
- CSS :	Applying styling across all pages.
- JavaScript	Add logic rules to all input forms and buttons.
- Python	Runs the entire backend server 

## Libraries
- Materialize:  Styling Framework to get a modern feel to the website.
- Font Awesome:	Used for all website icons.
- jQuery:	Simplifying some of the get id's for Javascript.
- Google Fonts:	For all fonts on all pages.

## Python Libraries
- Flask:	Required to run all route operations in the code.
- OS:	Required to read environmental variables.
- flask_pymongo:	Most search queries requires pyMongo to operate in the code.
- bson:	Required to acquire the object ID of the different data-sets.
- werkzeug.security	Required to operate hash for secure passwords.

## Database
- MongoDB	Store all content for the database for recipes and users.



# Testing
Due to all the features on the website, the testing have been broken up in multiple sections, each covering testing 
such as Intended use, Features, Responsiveness, Security and Code Testing, as well as Feedback. After all the tests 
there will be a summary section for a quick overview over all passed tests and bugs found. All tests will be preformed 
in Chrome, Firefox, and Edge on Desktop, and native IOS browser.

## I have tested the following

- Intended use (Interactivity)
- Responsiveness across devices
- W3 HTML Validator using URL and copy/paste code
- W3 CSS Validator
- JS Hint
- PEP8
## Intended Use on Chrome, Firefox and Edge (Interaction)
- Landing Page(Not logged in)
- Opening website on full screen expecting all images, icons, labels to be displayed with correct ratio.
- Clicking on a recipe  expecting it to open the accordeon to recipe correctly.
- Clicking Login to redirect me to login page.
- Clicking Register to redirect me to registration page.

## Recipe Page(Not logged in)
- Opening Recipe , expecting all icons, text to display correctly.
- Clicking on login to redirect me to login page.
- Clicking on register to redirect me to registration page page.
- Clicking "Grandma's Cookbook" get redirected to main landing page.

## Registration Page(Not logged in)
- Attempted putting in 1 letter into username, and left password  blank Expecting feedback on all input boxes.
- Attempted putting in 1 letter into username,  and add too short password Expecting feedback on all input boxes.
- Fixed username to 3 letters, left  password  too short still block user from register.
- Fixed password, now all registration rules are correct, allowing user to register, Expecting flash " Registration complete"

## Login Page
- Typed in username only and click login, asked for password.
- Typed in username and wrong password, -expected feedback, username and/or password incorect
- Typed in only password, but no username, was informed to type in username too.
- Typed in correct username and correct password, website allowed me to login.
- When logged in successfully, expecting the page to redirect user to landing page.

## Landing Page(Logged in)
- Expecting the navigation bar to no longer have Login and Register, but Logout Username  and Add recipe

## Recipe Page(Not author, but Logged in)
- Visiting Recipe page that my user have not made, expect to not see edit or delete buttons.
- view recipe correctly.
- Clicked website name to redirect to main page.
## Recipe Page(author, and Logged in)
- Visiting recipe page as author, expecting to see delete button and edit button 
- Clicking edit button redirect user to update page correctly.
- Clicking delete button, delete the recipe and redirect user to main page.


## Admin Login (only accessible when logged in as Administrator)
Clicking delete will remove any recipe from database.

## Create new recipe(Only accessible logged in)
- Attempting to submit the form empty, expecting to receive error message across the whole form.
- Adding 1 letter in recipe name, but is told it's too short.
- Adding more then 3, and get approved.
- Adding letters into portions,  also more than 2 numbers not passing the validation, informs user to add a number 1-99
- Adding number works.
- Adding ingredients, anything less then 5 characters will inform user it's too short.
- Adding How To steps, anything less then 8 characters will inform the user it's too short.

## Testing Bugs

Logo>> cut and stiled image from  openculture.com