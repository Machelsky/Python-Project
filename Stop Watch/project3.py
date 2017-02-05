
import simplegui


num=0  
counter1=0
counter2=0
msec=0
checkstop=True

def format(t):
    global msec
    min=t/600
    t%=600
    sec=t/10
    if sec<10:
        secstr="0"+str(sec)
    else:
        secstr=str(sec)
    t%=10
    msec=t
    return str(min)+":"+secstr+":"+str(msec)
    pass

def start():
    global checkstop
    timer.start()
    checkstop=True
def stop():
    global checkstop
    global counter1
    global counter2
    timer.stop()
    if checkstop:
        if msec==0:
            counter1+=1
        counter2+=1
        checkstop=False

def reset():
    global num
    global counter1
    global counter2
    timer.stop()
    num=0
    counter1=0
    counter2=0
    checkstop=True
    

def increase():
    global num
    num+=1


def draw(canvas):
    canvas.draw_text(format(num),[90,120],50,"White")
    canvas.draw_text(str(counter1)+"/"+str(counter2),(250,30),20,"Green")
    

frame=simplegui.create_frame("Stop Watch",300,200)
frame.add_button("Start",start)
frame.add_button("Stop",stop)
frame.add_button("Reset",reset)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,increase)

frame.start()