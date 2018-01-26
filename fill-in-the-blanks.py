# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

fib = ["___1___", "___2___", "___3___", "___4___"]

intro = """Please select a game difficulty by typing it in!
Possible choices include easy, medium, and hard:"""

easy_fill = """\n___1___(s) are named locations which are used to store references to the object stored in memory.
The names we choose for ___1___(s) and functions are commonly known as ___2___.  In python you dont need to declare
types of ___1___(s) ahead of time. Interpreter automatically detects the type of the ___1___ by the data it contains.
To assign value to a ___1___ equal sign ( = ) is used. = is also known as the ___3___ operator.  In Python ___4___(s)
are preceded by a pound sign ( # ).
"""
easy_answers = ["variable", "identifiers", "assignment", "comment"]

medium_fill = """\nPython has a ___1___() built in function which is used to determine the ___1___ of the variable.
% (percentage sign) operator also known as remainder or ___2___ operator. This operator returns remainder after division.
___3___ing points are values with decimal point. One point to note that when one of the operands for numeric operators is
a ___3___ value then the result will be in float value.  Strings in python are ___4___.  The definition of ___4___
is unchanging over time or unable to be changed.
"""
medium_answers = ["type", "modulus", "float", "immutable"]

hard_fill = """\nYou can take subset of string from original string by using [] operator also known as the ___1___ operator.
You can use ___2___ and not ___2___ operators to check existence of string in another string. They are also known as ___3___ operator.
The ___4___() function returns string by capitalizing first letter of every word in the string.
"""

hard_answers = ["slice", "in", "membership", "title"]

#Prompts user to choose a difficulty level from easy, medium, or hard
def level_diff():
    '''User to choose a difficulty level from easy, medium, or hard'''
    difficulty = ""
    options = ["EASY", "MEDIUM", "HARD"]
    while difficulty not in options:
        difficulty = raw_input().upper()
        if difficulty == "EASY":
            print "You've chosen Easy!"
            return easy_fill, easy_answers
        elif difficulty == "MEDIUM":
            print "You've chosen Medium!"
            return medium_fill, medium_answers
        elif difficulty == "HARD":
            print "You've chosen Hard!"
            return hard_fill, hard_answers
        else:
            print "Invalid input."

#Counts how many incorrect attempts were made before finding a correct answer.
#Returns a -1 when the aloud amount of guesses have been used.
def incorrect_answer(number_of_incorrects):
    '''Calculates the number of guesses per answer given.'''
    aloud_guesses = 5
    number_of_incorrects += 1
    if number_of_incorrects < aloud_guesses:
        print "\nSorry, try again.  You have " + str(aloud_guesses - number_of_incorrects) + " guesses left."
        return number_of_incorrects
    else:
        print "Sorry, Game Over.  You've used up all your guesses."
        return -1

#Takes the user input and sends it to the play_game function
def user_input(choice):
	'''Input from all answers provided from the user'''
	user_input = raw_input("\nEnter your answer for {} : ".format(choice)).lower()
	return user_input

#main function of the program, calls level_diff, user_input, and incorrect_answer
#This function will loop through until fib has no more options
def play_game():
    '''This is the main function of the game.'''
    num, incorrects = 0,0
    selected, answers = level_diff()
    while num < len(fib):
        print selected
        guessed_input = user_input(fib[num])
        if guessed_input == answers[num]:
            print "\nYou correctly answered that fill in the blank.\n"
            selected = selected.replace(fib[num], guessed_input)
            num += 1
            incorrects = 0
        else:
            incorrects = incorrect_answer(incorrects)
            if incorrects == -1:
                return
    print "You've answered all of the possible fill in the blanks. \nHere is the completed paragraph: \n"
    print selected

print intro
play_game()


# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
