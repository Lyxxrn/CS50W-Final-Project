# CS50W Final Project - Hompage

### The course: 
https://cs50.harvard.edu/web/2020/
## Content:

- [Additional Information](#Additional-Information)
- [Distinctiveness and Complexity](#Distinctiveness-and-Complexity)
- [The Files](#The-Files)
- [How to run the application](#how-to-run-the-application)

## Additional Information
I wanted to create this page not only as the final project for this course but also as a useful Homepage for a Club I am a member of. I come from Germany and wrote the whole frontend in German to archive this goal.

## Distinctiveness and Complexity

This Homepage completely meets completely the requirements for the final project. I used JavaScript, CSS and HTML for a mobile-responsive frontend to create a unique and goodlooking web page. For the backend I used the Django-Framework to program a small API and to manage the models. Because it is a Homepage I have focused more on the frontend than the backend to create a goodlooking page. 


## The Files

### The Backend

My Django App is calles 'verein' and it contains every files for both the front- and backend.

#### Models.py

1. User
    * a simple User-model from the Django 'AbstractUser'
    * Handles the admin account to create and edit new events and news
  
2. News
    * represents a news-page on the backend
    * contains title, content and the timsestamp
3. Event
    * represents a event-page on the backend
    * contains title, content and the timsestamp
4. The API
    * both Event and User are returning a Json-like object to pass the information to JavaScript 

#### Urls.py

This file is used to manage all the different routes both for the normal page and the API. The project is devided into to main websites. The first one is for the normal user while the second one is for administrative purposes. Here you can create new events, news and edit these while a normal user only can read threw them. 

#### Views.py

##### login_view / logout_view

* takes information from form and logs the admin in or out
* There is no registration page or function because only one administration account is needed and for safety purposes.


##### index

* just renders the main (index) page

##### member
* just renders the othe main (member) page for the administrator

##### news

* this gets the form data from the news-form and creates a new News object to be displayed on the main page


##### event

* this gets the form data from the event-form and creates a new Event object to be displayed on the main page

##### event_edit / news_edit

* renders the edit page with the initial values (existing model data)
* takes the form data and saves it to existing model after data is submitted

##### get_event / get_news

* these are the two API functions
* they simply respond with a Json-formatted array that contains all the events / news
  
### The Frontend

I made the front end without any Framework like Bootstrap or React to learn more CSS and JavaScript

#### templates

All HTML files are stored in this folder.

#### static

the images (mostly background) are saved in this folder.

#### static/functions
This file contains the frontend functions in JavaScript.

##### closeall

* simply hides all divs 

##### showOne

* first calls closeall to hide everything than show the selected div
* this is used to create the single page site

##### news

* sends a get request to the get_news function an creates new divs to display all the news pages 
* the user still has to click on the title to get to the whole news-page 

##### events

* sends a get request to the get_events function an creates new divs to display all the event pages 
* the whole event page is instantly portrayed (it does not take as much space as a news page)

##### edit_news / edit_events

* these are rendering a list of news / events 
* the admin has to click one of the list items to be forwarded to the edit page


#### static/functions
This file simply contains all the CSS code.

## How to run the application

1. Install Django:

    'py -m pip install Django'

2. configure the models
    'py manage.py makemigrations'

    'py manage.py migrate'

3. Run the applicaion

    'py manage.py runserver'