from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    label_2.config(text = "Timer")
    check_marks.config(text = "")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    Short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_2.config(text="Break", fg = RED)
    elif reps % 2 == 0:
        count_down(Short_break_sec)
        label_2.config(text = "Break", fg = PINK)
    else:
        count_down(work_sec)
        label_2.config(text = "Work", fg = GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) 
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label_1 = Label.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("DAY 28")
window.config(padx = 100, pady = 50, bg = YELLOW)


label_2 = Label(text = "Timer", fg = GREEN, bg = YELLOW , font = (FONT_NAME, 50))
label_2.grid(column = 1, row = 0)


button_1 = Button(text = "Start", highlightthickness = 0, command = start_timer)
button_1.grid(column = 0, row = 2)


button_2 = Button(text = "Reset", highlightthickness = 0, command = reset_timer) 
button_2.grid(column = 2, row = 2)

check_marks = Label(fg = GREEN, bg = YELLOW)
check_marks.grid(column = 1, row = 3)


canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness = 0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_image)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1 , row = 1)

window.mainloop()