# implementation of card game - Memory

import simplegui
import random
cards=range(8)+range(8)
exposed=[False for i in range(16)]
number1=0
number2=0
FONT=60
X_ADJUST=10
HEIGHT=100
WIDTH=50
Y_ADJUST=80

# helper function to initialize globals
def new_game():
    global state
    global turn
    global exposed
    state=0
    turn=0
    random.shuffle(cards)
    exposed=[False for i in range(16)]

     
# define event handlers
def mouseclick(pos):
    global state,turn,number1,number2
    card_pos=int(pos[0]/50)
    if not exposed[card_pos]:
        if state==0:
            state=1
            number1=card_pos
            exposed[card_pos]=True
            turn+=1
        elif state==1:
            state=2
            number2=card_pos
            exposed[card_pos]=True
        else:
            if cards[number1]!=cards[number2]:
                exposed[number1]=False
                exposed[number2]=False
            number1=card_pos
            exposed[number1]=True
            state=1
            turn+=1
    pass
  
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = "+str(turn))
    for card_index in range(len(cards)):
        cardpos=WIDTH*card_index+X_ADJUST
        if exposed[card_index]:
            canvas.draw_text(str(cards[card_index]),[cardpos,Y_ADJUST],FONT,"white")
        else:
            canvas.draw_polygon([[WIDTH*card_index,0],[WIDTH+WIDTH*card_index,0],[WIDTH+WIDTH*card_index,HEIGHT],[WIDTH*card_index,HEIGHT]],1,"red","green")
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric