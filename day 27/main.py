from tkinter import *

window  = Tk()
window.title("HI MY NAME IS VISHWAA")
window.minsize(500,300)
window.config(padx=20, pady=20)

my_label = Label(text = "AGAIN HI", font=("Arial", 24))
my_label.grid(column=0, row= 0)

#button

def button_clicked():
    print("IM CLICKED")
    a = input.get()
    my_label.config(text = a)
    # my_label.config(text= "I AM HAPPY")

button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)


#entry

input = Entry(width = 10) 
input.grid(column=2, row=2)


window.mainloop()