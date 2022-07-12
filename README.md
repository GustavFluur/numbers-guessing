# Number Guessing 
Number guessing is being run in a Python terminal game, which runs in the code institute mock terminal on Heroku.

Once the user is interacting with the game for the first time, they will find the introduction to be clear and concise. In short, you must choose a number between a span from the lowest - and to highest, plus you only have five chances to finish the game. 

[Here is the live version of the project to interact with - it will provide you a detail understanding on how the game operates. Enjoy!](https://numbers-guessing.herokuapp.com/)

![Responsive image](/assets/images/Responsitive%20image.png)

# Background 

Number guessing is game where the players simultaneously select an integer between between two numbers. In that span you must choose one per try, hence to figure out what number the computer has selected or hiding from the user. According to [wikipedia](https://en.wikipedia.org/wiki/Guess_2/3_of_the_average): Alain Ledoux is the founding father of the guess 
of the average-game. In 1981, Ledoux used this game as a tie breaker in his French magazine Jeux et Stratégie. He asked about 4,000 readers, who reached the same number of points in previous puzzles, to state an integer between 1 and 1,000,000,000. The winner was the one who guessed closest to of the average guess.

# How to play

In this game you have 5 chances to win and likewise no matter what result - you'll have options to either continue or to quit. The reason behind that feature is to create a sense of freedom for the user and preventing it for a sudden halt of its entertainment. 

## Updated gaming features:
#### Since the last submission was reccieved with some critics it has now been updated by added new content and features into the game for making it more appealing for the user's experience. 

Once you starting Number Guessing it says in the mock terminal:

       Try to guess the number (between 0 and 100) on five guesses!
        Enter guess 1: 

Depending how you guessed it the first time you'll receive an answer that goes align with the computer's secret number. If it's either high or low - until you hit it right. 

        Your guess is too high, please try again!
        Enter guess 3:

This is an example on how it indicates you won in the game, and no matter what result you get eventually the game is always shots down:

        Enter your guess 5: 25
        GREAT, YOU MADE IT ON THE SECOND TRY!
        Shuting down..


        Try to guess the number (between 0 and 100) on five guesses!
        Enter guess 1: 80
        Your guess is too high, please try again!
        Enter guess 2: 20
        Almost there, the number too low!
        Enter guess 3: 30
        Almost there, the number too low!
        Enter guess 4: 50
        Almost there, the number too low!
        Enter guess 5: 60
        Wow, you scored on try 5! HOW DID YOU KNOW!?
        Wanna try again?
        please press either y - yes or n - no
        y/n:






# Features

## Existing Features

## Ex 1.   
### As a summary from the previous section on how to play: you just follow the instructions from the terminal on what it says in game. Here in the first example you can tell the user won the game due to its feedback after its performance, as it shows here - it shows uppercase letters to highlight for the user that you done something great - won over the computer e.g. on the second try. Since it's quite challenging to score it right in the span between  0 - 100. 

        Try to guess the number (between 0 and 100) on five guesses!
        Enter your first guess: 50
        Your guess is too high, please try again!
        Enter your second guess: 25
        GREAT, YOU MADE IT ON THE SECOND TRY!
        Shuting down..

### *** Disclaimer: I forgot to add the first image of the winning example, and other ones were created right after, this will be added in the short future, thank you for your understanding***

## Ex2
### This is example shows it looks like when you are on the edge of loosing the game, that you got a score after the fourth and fifth try:
![4 tries - 1 score](/assets/images/4%20shots%20-%201%20score.png)
![5 tries - 1 score](/assets/images/Score%20on%20the%20last%20try.png)

## Ex 3
### The second example indicates an user's failure of the game and how it says in the end of it. What you need to do is to restart mock terminal to try again. 

![Failure after 5 chances](/assets/images/5%20tries%20-%20no%20win.png)

# Future Feature

* Create a score system to let the user know on how it's going and orientate itself over the process. 
* Add new content into the game, where you can change the level of difficulty. Give a sense of freedom and challenge.
* Reveal of the correct number, what the computer was hiding.

# Data Model

I decided to make this game as easy as possible due to lack of time and therefore the structure is easy built for the user and developers to take advantage from. Thus adding important imports to make it functional and a few inputs as well as prints. Nothing harder than that but as long as it's required and solid for the operating system to be as best it can be for the user. 

The vital method is the sys.exit() is to make the whole code structure to flow itself and not lose it's interest for user. But also stopping the loop and it can break away. The combination of prints makes it more fun for the user and in the inputs is vital to create an interaction as well. 


# Testing 

I have manually tested this project by doing the following:
* Passed the code through a PEP8 linter and confirmed there are no problems
* Given invaild inputs: strings when numbers are expected, out of bounds inputs, same inputs twice.   
* Tested in my local terminal and the Code Institute Heroku terminal. 


# Bugs 

### Solved Bugs

* No issues when it came to the coding and structure building of the python file, yet the only issue I encountered was some typing issues along with the development of the file. First, it’s hard to know what you want in the beginning and secondly, I got dyslexia, so missing out on some words or sentences is part of the process.  

# Remaining Bugs

 * No bugs to fix..       



# Validator Testing 


* PEP8

    * No errors were returned from PEP8online.com


* Exception:

    *  These messages won't stop the code to operate nor lower the the sense of entertainment in the game for the user.

![Results from PEP8online.com](/assets/images/PEP8.png)

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

