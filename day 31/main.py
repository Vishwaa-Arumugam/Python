import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
word = {}

try:
    data = pandas.read_csv("D:\\100P\\day 31\\data\\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("D:\\100P\\day 31\\data\\french_words.csv")
    word = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words)
    canvas.itemconfig(first_card_title, text="French", fill="black")
    canvas.itemconfig(first_card_word, text=current_word["French"], fill="black")
    canvas.itemconfig(old_image, image=flash_card_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(first_card_title, text="English", fill="white")
    canvas.itemconfig(first_card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(old_image, image=flip_image)


def is_known():
    words.remove(current_word)
    data_1 = pandas.DataFrame(words)
    data_1.to_csv("D:\\100P\\day 31\\data\\words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
flash_card_image = PhotoImage(file="D:\\100P\\day 31\\images\\card_front.png")
flip_image = PhotoImage(file="D:\\100P\\day 31\\images\\card_back.png")
old_image = canvas.create_image(400, 263, image=flash_card_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
first_card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
first_card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

button_tick_image = PhotoImage(file="D:\\100P\\day 31\\images\\right.png")
button_tick = Button(image=button_tick_image, highlightthickness=0, command=is_known)
button_tick.grid(row=1, column=1)

button_cross_image = PhotoImage(file="D:\\100P\\day 31\\images\\wrong.png")
button_cross = Button(image=button_cross_image, highlightthickness=0, command=flip_card)
button_cross.grid(row=1, column=0)

next_card()

window.mainloop()
