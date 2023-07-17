from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =0.1
SHORT_BREAK_MIN = 0.15
LONG_BREAK_MIN = 0.1

reps = 0
timer= None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text= "00:00")
    title_lable.config(text= 'Timer')
    check_marks.config(text='')
    global reps 
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    # Hold on the REPS and update them
    global reps
    reps += 1
    #  count_donwn Patterns
    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        title_lable.config(text='Work Time', fg= GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_lable.config(text='Relax,You have earned it!!', fg= RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_lable.config(text='Short Break!', fg= PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
## Create Funtion
def count_down(count):

    # Create clock
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count % 60}'
    

    # Access CANVAS.ITEMCONGIG(function, passing **kwargs)
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        # Window WAITS (time ms, function, passing *args)
        global timer
        timer= window.after(1000, count_down, count-1)
    else:
        # if Count is = or - than 0
        start_timer() # Start Function
        
        ## Compile the CheckMarks
        marks= ''
        work_sessions= math.floor(reps/2)
        for work_sessions_completed in range(work_sessions):
            marks += '✔'
        check_marks.config(text= marks)



# ---------------------------- UI SETUP ------------------------------- #

## Window's Config
window= Tk()
window.title ('Pomodoro')
window.config(padx= 100 , pady= 50, bg= YELLOW)


## Windows Items ##
###################

## Title
title_lable = Label(text= 'Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME,50))
    # Title Position 
title_lable.grid(column=1, row=0)



## Background Image
    # Img config
canvas= Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
    # Txt Cnfig
timer_text=canvas.create_text(100, 140, text = '00:00', fill= 'white', font=(FONT_NAME,30,'bold'))
    # Canvas Position 
canvas.grid(column=1,row=1)

## Buttons
    # START Button
start_button= Button(text= 'Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2) # Position
    # RESET Button
reset_button= Button(text= 'Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=2) # Position

## Check Marks
check_marks= Label(fg=GREEN, bg= YELLOW, font=(FONT_NAME,20,'bold'))
    # Position
check_marks.grid(column=1, row=3)


## Keeps Window runing
window.mainloop()
