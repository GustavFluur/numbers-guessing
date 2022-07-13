# Number Guessing 
Number guessing is a Python terminal game, which runs in the code institute mock terminal on Heroku.

Once the user is interacting with the game for the first time, they will find the introduction to be clear and concise. In short, you must choose a number between a span from the lowest to highest, plus you only have five chances to finish the game. 

###### *Disclaimer: The project and its readme file has been recently updated - from June 10th 2022 to July 12th 2022. It has now been added new content and features into the game for making it more appealing for the user's experience. Due the last submission was reccieved with some critics over the codeblock's missing necessary characteristics has made Number Guessing optimized.   

[Here is the live version of game to interact with - it will provide you a detail understanding on how the game operates. Please enjoy!](https://numbers-guessing.herokuapp.com/)

![Responsive image](/assets/images/Responsitive%20image.png)

# Background 

Number guessing is game where the players simultaneously select an integer between between two numbers. In that span you must choose one per try, hence to figure out what number the computer has selected or hiding from the user. According to [wikipedia](https://en.wikipedia.org/wiki/Guess_2/3_of_the_average): Alain Ledoux is the founding father of the guess 
of the average-game. In 1981, Ledoux used this game as a tie breaker in his French magazine Jeux et Stratégie. He asked about 4,000 readers, who reached the same number of points in previous puzzles, to state an integer between 1 and 1,000,000,000. The winner was the one who guessed closest to of the average guess.

# How to play

In this game you have 5 chances to win and likewise no matter what result - you'll have options to either continue or to quit. The reason behind that feature is to create a sense of freedom for the user and preventing it for a sudden halt of its entertainment. 

## Updated gaming features: 

Once you starting the Number Guessing game it still says in the mock terminal:

       Try to guess the number (between 0 and 100) on five guesses!
        Enter guess 1: 

What it does the player will be given instructions and a purpose for the user to be encouraged on how to play the game. As it was in the previous version - it depends on what numbers of your choice are being typed into the terminal thus you’ll receive a message: If your number is either high or low – the system is therefore signaling if you are on the right track, but keeping the computer’s secret number disclosed.  

        Your guess is too high, please try again!
        Enter guess 3:

This is an example on how indicated in the previous version you won the game, and no matter what result you get eventually the game is always shots down:

        Enter your guess 5: 25
        GREAT, YOU MADE IT ON THE SECOND TRY!
        Shuting down..

However, as it shows in the last message in the terminal the game was being shut down and you were unable to continue - that restriced the entertainment and a desire to look for previous results was prevented: 

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


In the last message you either press "y" and "n" (in small letters). Therefore the updated version was needed and creating a sense of gaming loop until the player to decides to finish or to carry on with the game.  

        Wow, you scored on try 5! HOW DID YOU KNOW!?
        Wanna try again?
        please press either y - yes or n - no
        y/n:y
        Try to guess the number (between 0 and 100) on five guesses!
        Enter guess 1: 


# Features

## Existing Features

  
##### This section we are going to walk through the processes and features of the game. What the user is experiencing and encounter step by step. For making it clear and explicit we are going to use the random examples that is being portayed in the game and the mock terminal on Heruko.  

## Ex 1. 
##### Here in the first example you can tell the user won the game due to its feedback after its performance, as it shows here - it shows uppercase letters to highlight for the user that you've won over the computer e.g. on the fourth try after the player decided to continue the game. Since it's quite challenging to win over the computer with the right number in the span between  0 - 100 it generates a benefit for the player and by doing this it creates an encourgement to willing to carry on with the game. 
![score](/assets/images/score.png)


## Ex2
##### What happens if you type a letter or something else into the terminal that shouldn't be there? Well, the game is sending a message back to the user : "Please enter a number!". It's a simple communication directed to the participating player to only write a number and gives an understanding the rules of the game. Please look at the example below: 
![digits&numbermix](/assets/images/digits&numbermix.png)
##### It dosen't matter how many times you are writing false inputs into the terminal - you still recieve the same answer: "Please enter a number!" and it wont hurt the outcome of the game. Thus you can carry it on without any issues. 
![No numbers in the game](/assets/images/no-numbers.png)
![No numbers in the game 2](/assets/images/no-numbers_continuegame.png)

## Ex 3
##### A feature that has been shown in the previous examples are the button that says: "please press either y - yes or n - no" after the round is done. It gives an opportunity for the player to either continue or to leave the game. As well as wrong inputs while you suppose to type in numbers - the function works the same where nothing breaks as the player is typing it all wrong - just until you got it all right in the end. 
![Fasle inputs into y-n button](/assets/images/y-n-wrong.png)

## Ex 4
##### The final example. How does it look once you desire to finish the game or to press "n"? As you do you are unable to continue and system will make you exit the terminal. Thus it indicates you will no longer be able to play Number Guessing at this time and likewise it communicates well for the player to realize that the game is now finish - if you want to restart then you need to refresh the page on the Python Terminal by Code Institute. 
![Goodbye!](/assets/images/goodbye.png)

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

##### No issues when it came to the coding and structure building of the python file, yet the only issue I encountered was some typing issues along with the development of the file. First, it’s hard to know what you want in the beginning and secondly, I got dyslexia, so missing out on some words or sentences is part of the process.  

# My failed Codeblock 

###### My first submission was conducted in a fast pace and that led to missing valuable functions that was required to pass this python based project and therefore I came with this updated code block after my second try, which I hoped for a good result. 

###### Yet, it was another misstake because it had still missing functions, bad inputs and not clear structured code etc. to fully understand what is going on within its system. That led to I took action to contact my mentors for some extra guidance and support. That gave me the learnings and some valuable insight to execute this task with better standards than the last two submissions. 

###### For future and present coders this is how my updated code block looked like after my second submission and the reason I want to show you this is to learn by my own misstakes. To prevent a verbose readme file - please check the image here with the current python code (run.py) what changes have made:  
![My uppdated Codeblock](/assets/images/codeblock_prev.png)

###### In the begnining of my codeblock it had severe missing elements that required and I didn't typed in since I was following an educational video on YouTube [Beginner Python Project: Number Guessing Game](https://www.youtube.com/watch?v=tKjL670MARY) and wanted to make the code simple as possible for handing in the project as fast I could. I should have paid more attention to the projects critera requirements instead of code along. It's imperative to understand what those are but it's absolutely fine to take inspiration from wherever you want. 


# Validator Testing 


* PEP8

    * No errors were returned from PEP8online.com
    * One warning on line 64 - won't make any errors nor bugs in the code as a whole. 


* Exception:

    *  These messages won't stop the code to operate nor lower the the sense of entertainment in the game for the user.

![Results from PEP8online.com](/assets/images/pep8_new.png)

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



# Credits to my mentors

I want to thank my previous and current mentors on Code Institute, who guide me to build a new and structured Codeblock. Without their support, advice and inspiration it would have been much harder to understand what I missed: 

- Sandeep Aggarwal 
- Martina Terlevic  

Thank you!

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

