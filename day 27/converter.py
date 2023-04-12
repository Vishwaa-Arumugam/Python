from tkinter import *

window = Tk()
window.title("Mile to kilometer Converter")
# window.minsize(300,100)
window.config(padx=20, pady=20)


label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text="Km")
label_2.grid(column=2, row=1)

label_3 = Label(text="is equal to")
label_3.grid(column=0, row=1)

label_0 = Label(text="0")
label_0.grid(column=1, row=1)

input = Entry(width=7)
input.grid(column=1, row=0)


def calculate():
    a = input.get()
    label_0.config(text = int(int(a) * 1.609))

button = Button(text="Calculate", command=calculate)
button.grid(column=1 ,row=2)




window.mainloop()