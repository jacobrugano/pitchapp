## Project: Pitches
 ------------------------------------------------------------
## Project Description
 ------------------------------------------------------------
This is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application

 ------------------------------------------------------------
### Live link:
 ------------------------------------------------------------
## User story
1) Comment on the different pitches posted py other uses.
2) See the pitches posted by other uses.
3) Vote on s pitch they have viwed by giving it a upvote or a downvote.
4) Register to be allowed to log in to the application
5) View pitches from the different categories.
6) Submit a pitch to a specific category of their choice.

 ------------------------------------------------------------
## BDD
 ------------------------------------------------------------
This shows the Behaviour, the Input	and the Output.
1) Load the page, on page load, get all posts, Select between signup and login
2) Select SignUp, enter Email,Username,Password	and you will be Redirected to the login
3) Select Logins (Username and password), and you will be redirected to page with app pitches based on categories and commenting section
4) Click the comment button, and input your comment
5) Click on submit button and you will be redirected to all comments tamplate with your comment and other comments
Development Installation
 ------------------------------------------------------------
## Cloning the repository:
------------------------------------------------------------
1) Copy this link:https://github.com/jacobrugano/pitches.git
2) Navigate to the folder and install the requirements
3) cd into pitches
4) pip install -r requirements.txt
5) Export Configurations
6) export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
7) Run the application
8) python3.6 manage.py server
9) Test the application by running this command on the terminal python3.6 manage.py test
10) Open the application on your browser 127.0.0.1:5000.
 ------------------------------------------------------------
## Technology used
------------------------------------------------------------
Python3.6
Flask
Heroku

------------------------------------------------------------
## Known Bugs
------------------------------------------------------------
There are no known bugs currently but pull requests are allowed incase you spot a bug

------------------------------------------------------------
## Contact Information
------------------------------------------------------------
If you have any question or contributions, please email me at [jacobrugano@gmail.com]

------------------------------------------------------------
## License
------------------------------------------------------------
MIT License:
Copyright (c) 2022 Jacob Rugano
- ------------------------------------------------------------
