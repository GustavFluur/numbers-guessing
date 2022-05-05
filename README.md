# Number Guessing 
Number guessing is being run in a Python terminal game, which runs in the code institute mock terminal on Heroku.

Once the user is interacting with the game for the first time, the introduction of it is clear and concise. Where you must choose a number between a span of the lowest and highest, plus you only have five chances to finish it.  

[Here is the live version of the project to interact with. Here it will provide you a detail understanding on how the game operates. Enjoy!](https://numbers-guessing.herokuapp.com/)

![Responsive image](/assets/images/Number-guessing-image1.png)

# How to play


# Features

## Existing Features

## Header 
![Header](/assets/images/)

- [text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][t

## Greeting & Introduction
![Greeting](/assets/images/intro.png)

- [text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here]
- [text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here]
- [text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here][text here]

## The Game Option
![Responsive image](/assets/images/Scissor-zom.png)

## Gaming Result
![Responsive image](/assets/images/gaming-results.png)

## Favicon 
![Favicon](/assets/images/favicon.png)

# Testing 
- Tested the webpage on these browsers: Brave Browser, Chrome, Firefox and Safari. 
- I confirmed that the game results are always correct.
- I confirmed that header, instructions, item selection and results are readable and easy to understand. 
- I confirmed that the colors and fonts chosen are easy to read and acessible by running the lighthouse: 

**To save some time and easy to conduct the lighthouse I was only able to come up with lighthouse figures in Swedish, therefore you'll have the English Translation here:**

**Prestanda: Performance**
**Tillgänglighet: Accessibility**
**Bästa Metoder: Best Practices**
![lighthouse](/assets/images/lighthouse.new.png)

# Features left to implement

# Validator Testing
## HTML
Two errors were found within HTML file but no need to change them since it dosen't stop the overall game to function.

## CSS
Two error were found, but was later fixed. 

## JavaScript

In the JS validator there were 13 warnings found within the JS file and unused function, that was being removed from the file. The 13 warnings states because it won't hurt the overall function of Rock, Scissor and Paper game. 


# Bugs 

### Solved Bugs

# Validator Testing 
    - PEP8
        - 

# Deployment

This project was deployed on using Code Institute's mock terminal for Heroku.

Steps for deployment:

1. Fork or clone this repository
2. Create a new Heroku app
3. Set the buildpacks to Python and NodeJS in that order
4. Click on Deploy


## Disclaimer!

The connection between GitHub and Heroku hasn't been running as expected, which means you were forced to use all the 
installation through the terminal on GitPod. 


## Deploying your app to heroku:

1. Login to heroku and enter your details.
command:    heroku login -i

2. Get your app name from heroku.
command:    heroku apps - heroku logs -a numbers-guessing --tail

3. Set the heroku remote. (Replace <app_name> with your actual app name)
command:    heroku git:remote -a <app_name>

4. Add, commit and push to github
    command:    git add . && git commit -m "Deploy to Heroku via CLI"

5. Push to both github and heroku
command:    git push origin main
command:    git push heroku main



# Credits 
## Content 

- Code Institute for deployment terminal
- Wikipedia for the details of Number Guessing game & [Influence was taken from website: Math is fun.](https://www.mathsisfun.com/games/guess_number.html)

Sites that gave me the support and inspiration for building the app were: 
1. [freeCodeCamp - Back End Development and APIs](https://www.freecodecamp.org/learn/)
2. [CodeCademy - Course: Learn Python 2](https://www.codecademy.com/)
3. [12 Beginner Python Projects - Coding Course](https://www.youtube.com/watch?v=8ext9G7xspg)
4. [Beginner Python Project: Number Guessing Game](https://www.youtube.com/watch?v=tKjL670MARY)
5. [Guess the Number Beginner Python Tutorial | Learning Python for Beginners | Code with Kylie #8](https://www.youtube.com/watch?v=ZsRMQHbx6Xc)
6. [Geeks for Geeks: Number guessing game in Python 3 and C](https://www.geeksforgeeks.org/number-guessing-game-in-python/)
7. [StackOverFlow: Last try for guesses and Try/Except in Guess The Number game](https://stackoverflow.com/questions/67330299/last-try-for-guesses-and-try-except-in-guess-the-number-game)

