# The Top Shelf

The Top Shelf is a website for all your cocktail needs. Featuring cocktail recipes for 9 categories of alcohol from Gin to Whiskey and even some Mocktails. Users can register an account to allow them to add a new recipe to the website or edit any existing recipe that they had previously added. 
 
## UX

#### Wireframes
##### Homepage
[Desktop](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Desktop-Homepage.png)
[Mobile](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Mobile-Homepage.png)


#### Database Schema
The database schema that I sued for the project can be found [Here]()

#### About the Website
This website is for anyone who may need a cockatil recipe for an event they are hosting or if they just want to expirement with any alcohol they have at home. 

The Top Shelf website allows the user to easily navigate by selecting an alcohol that they wish to be the base of their recipe. They are then presented with a list of cockatils that are can be produced from the selected Alcohol. Once the user selects a cocktail they are presented with a list fo the ingredients required to make the cocktail, followed by the instructions on how to make it.

If a user comes across a new cockatil recipe that they wish to add to the website, thye can easily do so. They need to navigate to the login page where they should register as a new user. Once registered, they need to login with their username and password. After they have logged in they should navigate to the 'Add a Cockatil' page where they can provide all the required information to add their favourite new cocktail to the website.

A logged in user who is returnign to the website can view a list of all the cocktails that they have uplaoded to the website in the past. From there they can edit an existing recipe if they have found a nicer recipe for the cocktail. They can also delete the recipe if they don't wish it to be on display.

A user who is looking for a non-alcolohic cockatil would navigate to the Mocktails section of the website from the home page, here they will find a list of the non-alcoholic cocktails.


## Features
 
### Existing Features
- View Cockatails by Category - From the homepage with one click a user can get a list of coketails from their chosen category
- Register/Login - Users can easily register as a new user or login as an existing user from the login page.
- Logged In Users can fill in the form on the 'Add a cockatil' page to add a new cocktail tot eh website.
- Logged In users can edit their existing recipes or delete them if they don't wish to show them again


### Features Left to Implement
- Allow the user to upload images for their cocktails from their local devices instead of them having to provide a URL

## Technologies Used


- [Flask](https://palletsprojects.com/p/flask/)
    - The project uses **Flask** and **Python 3** to render the HTML webpages. Flask is a micro web framework written in the Python programming language. Flask has many resources that aid with the development of web apps. Some of the resources I used were:
         - render_template
         - redirect
         - request
         - url_for
         - session

- [Jinga2](http://jinja.pocoo.org/)
    - The project uses the **Jinga2** templating engine to add dynamic content to the various webpages throughtout the project. Jinga2 allows the use of loops and conditional statements. 

- [Materialize CSS](https://materializecss.com)
    - The project uses **Materialize CSS** for general page styling and layout.

- [jQuery](https://jQuery.com)
    - The project uses **jQuery** to make sure some of the Materialize CSS components (dropdown menus in forms, image sliders & modals) work correctlty. jQuery was also used to allow extra ingredients and instructions be added to the 'Add a cocktail' form.

- [Material Icons](https://material.io/tools/icons/)
    - The project uses **Material Icons** for any icons that are used in the website. The use of icons makes the website easier to read and understand for the user.

- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google Fonts** for the Playfair font that is used throughout the website.


#### To be completed