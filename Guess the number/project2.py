# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range=100
# helper function to start and restart the game
def new_game():
    global secret_number
    global num_range 
    global count
    print "New game. Range is from 0 to "+str(num_range)
    if num_range==100:
        secret_number=random.randrange(0,100)
        count=7
        print "Number of remaining guess is "+str(count)
    else:
        secret_number=random.randrange(0,1000)
        count=10
        print "Number of remaining guess is "+str(count)



# define event handlers for control panel
def range100():
    global num_range
    global count
    num_range=100
    count=7
    new_game()

def range1000():
    global num_range
    global count
    num_range=1000
    count=10
    new_game()
    
def input_guess(guess):
    global count
    number=int(guess)
    print "Guess was",number
    if number>secret_number:
        print "Higher"
        count-=1
        print "Number of remaining guesses is "+str(count)
    elif number<secret_number:
        print "Lower"
        count-=1
        print "Number of remaining guesses is "+str(count)
    else:
        print "Correct"
        new_game()
        
    if count==0:
        new_game()

f=simplegui.create_frame("Guess the number",200,200)
f.add_button("Range is [0,100)", range100,200)
f.add_button("Range is [0,1000)", range1000,200)
f.add_input("Enter a guess", input_guess, 200)

    
# create frame


# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
