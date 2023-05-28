from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password = password_letters + password_numbers + password_symbols
    shuffle(password)
    new = "".join(password)

    label_3_input.insert(0, new)

    # pyperclip.copy(password)

def save():
    website = label_1_input.get()
    email = label_2_input.get()
    password = label_3_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please enter all fields")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details:\nEmail: {email}\nPassword: {password}\n is it ok to save ?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data) # to update a json data without changing the format ##
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                label_1_input.delete(0, END)
                label_3_input.delete(0, END)
        else:
            label_1_input.delete(0, END)
            label_3_input.delete(0, END)
            save()
            
def find_password():
    website = label_1_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

# labels

label_1 = Label(text="Website:", font=("Arial", 10))
label_1.grid(column=0, row=1)

label_2 = Label(text="Email/Username:", font=("Arial", 10))
label_2.grid(column=0, row=2)

label_3 = Label(text="Password:", font=("Arial", 10))
label_3.grid(column=0, row=3)

# Entries

label_1_input = Entry(width=21)
label_1_input.grid(column=1, row=1)
label_1_input.focus()

label_2_input = Entry(width=39)
label_2_input.grid(column=1, row=2, columnspan=2)
label_2_input.insert(0, "vishwaa@gmail.com")

label_3_input = Entry(width=21)
label_3_input.grid(column=1, row=3)

# buttons

button_1 = Button(text="Generate Password", command=generate_password)
button_1.grid(column=2, row=3)

button_2 = Button(text="Add", width=18, command=save)
button_2.grid(column=1, row=4, columnspan=2)

button_3 = Button(text="Search", width=13, command=find_password)
button_3.grid(column=2 , row=1)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="1.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

window.mainloop()
