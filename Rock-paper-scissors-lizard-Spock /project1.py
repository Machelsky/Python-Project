# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    if name=='rock':
        return 0
    elif name=='Spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4
    else:
        print "Wrong name"

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    if number==0:
        return 'rock'
    elif number==1:
        return 'Spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    elif number==4:
        return 'scissors'
    else:
        print "Wrong number"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    print "                       "
    # print a blank line to separate consecutive games
    print "Player chooses "+player_choice
    # print out the message for the player's choice
    player_number=name_to_number(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    comp_number=random.randrange(0,5)
    # compute random guess for comp_number using random.randrange()
    comp_choice=number_to_name(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print "Computer chooses "+comp_choice
    # print out the message for computer's choice
    difference=(player_number-comp_number)%5
    # compute difference of comp_number and player_number modulo five
    if (difference==1 or difference==2 or difference==-3 or difference==-4):
        print "Player wins!"
    elif difference==0:
        print "Even game!"
    else:
        print "Computer wins!"
        
    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


