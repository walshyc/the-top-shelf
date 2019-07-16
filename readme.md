# The Top Shelf

The Top Shelf is a website for all your cocktail needs. Featuring cocktail recipes for 9 categories of alcohol from Gin to Whiskey and even some Mocktails. Users can register an account to allow them to add a new recipe to the website or edit any existing recipe that they had previously added. The project uses MongoDB as the database to store all the information and recipes for the website.

The project can be viewed [here](http://the-top-shelf.herokuapp.com/)
 
## UX

#### Wireframes
##### Homepage
[Desktop](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Desktop-Homepage.png)
[Mobile](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Mobile-Homepage.png)

##### Category Page
[Desktop](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Desktop-Category.png)
[Mobile](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Mobile-Category.png)

##### Add a Cocktail
[Desktop](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Desktop-Add_a_drink.png)
[Mobile](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Mobile-Add_a_Drink.png)

##### Single Cocktail
[Desktop](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Desktop-single_drink.png)
[Mobile](https://raw.githubusercontent.com/walshyc/the-top-shelf/master/static/img/wireframes/Mobile-single_drink.png)


#### Database Schema
The database schema that I sued for the project can be found [Here](https://github.com/walshyc/the-top-shelf/blob/master/static/schema.txt)

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

- [MongoDB](https://mongodb.com)
    - The project uses **MongoDB** to store all the recipes and user information. CRUD (create, read, update & delete) tasks are preformed on the database when users login, register, add a new cocktail, delete a new cocktail etc.

- Bycrypt
    -This project uses Bycrypt to store and encrypted hashed version of a users password in the database. By hashing a user password the password is stored more securly.



## Testing
#### Validation

I ran all the HTML file's through a HTML validator on [HTML Validator](https://validator.w3.org). SOme pages initially showed up with errors as I had forgot to use the ALT attribute on quite a few images. I went back and rectified this. On the single cocktail page I also had a an open span tag that was never closed, so I removed the tag.

I used [CSS Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file style.css, this proved to be all correct.

I also used [Color.review](https://color.review/) to to select the Cyan color from the Materialize CSS color palette as this color worked good with both black and white text.

#### Browser Support

I have tested the site functionality across Google Chrome, Safari & Firefox on both desktop and mobile viewports. I tested the website across a number of devices also - Windows Desktop, Macbook, Apple iOS on iPhone 7 and iPad Pro and on a Huawei P20. I also used the Google Chrome developer tools to simulate a number of other devices to ensure the website displayed and wqorked correctly. The website required a few minor changes to ensure it worked corectly and looked the same across each browser and on the devices I used for testing.


#### Login/Register

I have simulated a number of scenarios on the login and register process. I decided the make the username case insensitive to make the process more user friendly. I tried to register as a new user without suppling a password which failed as expected. I also tried to login with incorrect username and password combinations which also failed. Another simulation I preformed was where I tried to register a new user with a username that already existed, this also failed.

#### Adding a New Cocktail

On the Add Cocktail page the user must fill in each element of the form before they can sumbit the new recipe to the database. I tried on numerous occassions to submit the form with a seperate input missing from the form on each occassion. The form did not submit and a message is displayed to the user that they need to fill in all elements of the form.

The user can add extra ingredients or step inputs by using th ebuttons provided. I tested the adding and remove buttons and they worked as I wished.

#### Editing a Cocktail

When a user wishes to edit a cocktail the form is pre populated with all the existing information on the selected cocktail. I tested editing one piece of data on a cockatil and also adding and removing new ingedients and instruction steps. The cocktail record was updated int he database as expected with each test.

## Deployment

### Github

I regulary committed changes to Github thorugh the source control feature on Visual Studio Code. I used a short commit message to reflect each new change that was made in each commit. At last count I had over 60 commits on this project.

After I had completed each minor step on the website such as getting the Google Map to appear, getting the country buttons aligned correctly I committed the changes to the Github repository along with a short message. This made it easy to fall back on old commits when needed.

### Heroku

I used [Heroku](https://www.heroku.com/) to deploy the project. The project can be viewed [here](http://the-top-shelf.herokuapp.com/).

After each commit to Github I would use the command 'git push heroku master' in the terminal to push the project to Heroku so that the latest version of the site could be viewed.

I had to create a Procfile and a requirements.txt file in the root of my project to deploy it successfully to Heroku. The Procfile tells Heroku what commands it needs to run. The reuqimrenets.txt file tells Heroku what Python librarires it needs to install for the project to run correctly.

Heroku also required some Envirnomental Variables to be added for the IP, PORT and the MONGO_URI which is the link to the MongoDB database.

I created 4 test users to help with testing the website functionality and populating the database with the usernames - david, susan, claire and tom. The password for each acount is password. Each user has a number of cocktails added by them. The username david has the most cocktails added to the database.

## Credits

I took all cocktail recipes and images from the [BBC Good Food](https://www.bbcgoodfood.com/) website. I used a number of lectures from the Code Institute course to help me with the project as well as Stack Overflow and videos from YouTube on Flask Web Development.