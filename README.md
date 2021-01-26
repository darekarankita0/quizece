# Code Institute - Milestone Project 3 - [Riddle Me This...](https://tolkien-riddle-quiz.herokuapp.com/)
#### by Patrick Doherty

The brief I was given for this project was the following:

#### CREATE A 'RIDDLE-ME-THIS' GUESSING GAME
Build a web application game that asks players to guess the answer to a pictorial or text-based riddle.
The player is presented with an image or text that contains the riddle. Players enter their answer into a textarea and submit their answer using a form.
If a player guesses correctly, they are redirected to the next riddle.
If a player guesses incorrectly, their incorrect guess is stored and printed below the riddle. The textarea is cleared so they can guess again.
Multiple players can play an instance of the game at the same time, each in their own browser. Users are identified by a unique username, but note that no authentication features such as a password are required for this project.
Create a leaderboard that ranks top scores for all (at least recent) users.

#### I completed this brief and on the suggestion of my mentor I went and converted into a one-page app with the use of javascript. If the user's browser has disabled javascript it will revert to the normal multi-page app.

## UX
#### User stories
1. User will be directed to a login page and asked for a username, no password neccessary. The username will then be validated with some 
basic criteria. Once a username is acceptable the user will be directed to the first question of the quiz. 
2. The user is presented with a picture and a riddle. They have the option to submit an answer or skip the question. 
3. If the user enters the correct answer they are directed to the next page where their updated total is displayed.
4. If they answer a question incorrectly they will be given an error message and it will remain on the same page until the correct answer is given.
5. If the user chooses to skip the question they will move on to the next question. 
6. Once the user has attempted/skipped 10 questions they will be redirected to the leaderboard which will display a message depending on their score.
7. The leaderboard is accessible even if the user has not logged in, although they will not recieve a message as they have not submitted a score.


## Features

### Existing Features
- Simple Quiz App

### Potential future features
- Quiz - Users can upload quiz questions, if they are approved they can be added to a bank of questions. Users can then take a quiz made from these questions and compare results
on a scoreboard.
- Use a database instead of .txt file. 
- Create authentication to protect usernames for individuality on the site. 


## Technologies used:
##### HTML - a standardized system for tagging text files to achieve font, colour, graphic, and hyperlink effects on World Wide Web pages.
##### CSS - cascading style sheets to style the content and layout of the site.
##### Javascript - client side scripting language for asynchronous devlopment
##### Python - Programming Language to create the backend that decides upon the responses to the user's input.
##### Git Bash & GitHub -for version control and backup of code
##### Bootstrap - A framework for developing responsive, mobile 1st websites.
##### Flask - python web framework
##### Postman - Postman helps you develop APIs faster
##### Libraries I needed to install
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation, and allow for AJAX requests.

## Testing
 
### Automated testing

#### TDD
To ensure I was designing functions correctly I used tests to drive development. The majority of these can be found in helper_tests.py.
I could not write tests for all functions especially those required to write, retrieve and operate on data in a text file. I did however print my results
whilst designing the functions. I would also be able to check the text file itself to see if everything was working. I would also compare these to what 
the site was rendering, over and over again until I was getting the results I wanted. 

#### Test Suite
Once I was happy with the site I used unittests to do fully automated tests of the quiz app. I simulated a user logging on, and then going through each of the questions
eventually leading to the leaderboard. I also made sure to do a few runs, including incorrect answers and question skips. I made sure to 
test for the correct responses whther they were based on final score or incorrect answers. These can be found in test_app.py. All routes were tested including
the routes specifically for javascript. I also used Postman to check that I recieving the correct HTML when sending information to routes.

### Manual testing
#### Preventing Cheating
During my development I tried to break the game as often as possible, this seemed to be most easy by pressing the back button. I had originally designed the 
app to have a specific url for each question and users could simply visit these urls and answer the questions again. I removed this possibility by using
"sessions". This would allow for tracking a users progress and ensuring they could not go backwards or forwards or potentially answer any question
they were not supposed to. 

At the very end of my testing I noticed I was using a value from a hidden input (the solution to the question) to validate the answers. Anyone who could 
open dev tools could see this and simply copy it. They could even change it and that would work as the new solution. I removed this possiblity and found 
a simple work around. 

#### Cross-browser Testing
I developed the site mainly on Chrome but have also since tested it on Safari and Firefox with no issues.
All user stories have been checked with developer tools for their responsiveness. 
Through this method I tested a wide variety of devices; iPhone 5,6,7,8,X, 
iPad, iPad Pro, Google Pixel 2 and Galaxy S5. I am very happy with how my project scales on different devices.

#### Code Validation
I ran all my files through validators to check for errors.
    - W3C for CSS.
    - W3C for HTML.
    - JS Hint for Javascript
    - PEP8 online checker for Python

## Deployment
- Project was deployed to heroku with ease.
- Only major difference between development and production is the need to import env file for unittests in development site.
- Created Procfile and requirements.txt
- Created new heroku app and set environment variables.
- Linked my github and environment with heroku.
- Pushed to heroku. Click [here](https://tolkien-riddle-quiz.herokuapp.com/) to visit the site.

## Credits

### Media
- All of the original links the images used can be found in /data/riddle_data.json. All taken from google image searches. 


### Acknowledgements
- J. R. R. Tolkien for his timeless riddles.
- Thanks to the following Youtubers for sharing their knowledge
    - [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)
    - [Tekboi Tutorials](https://www.youtube.com/channel/UCIx6RlgCn3dXR5mHF33_wsA)
