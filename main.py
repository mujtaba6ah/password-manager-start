from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    passwords = "".join(password_list)

    password_entry.insert(0, passwords)
    pyperclip.copy(passwords)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def sav():
    website = website_entry.get()
    emil = user_emile_name_entry.get()
    passwords = password_entry.get()
    new_data = {
        website: {
            "email": emil,
            "password": passwords,
        }
    }

    if len(website) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Ops", message=" Please don't Let it empty ")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- find password ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="NO data", message="no data file fond ")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email:{email}\n password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f" {website} not exist ")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# the logo canvas:
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(120, 120, imag=pass_img)
canvas.grid(column=1, row=0)

#  the lalbls:
website_liable = Label(text="Website:")
website_liable.grid(column=0, row=1)
user_emile_name = Label(text="Username/Email:")
user_emile_name.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# user entry:
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
user_emile_name_entry = Entry(width=35)
user_emile_name_entry.grid(column=1, row=2, columnspan=2)
user_emile_name_entry.insert(0, "mujtabaabdelgadir@gmail.com")

password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate password", width=12, command=password_generate)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=sav)
add_button.grid(column=1, row=4, columnspan=2)

search = Button(text="search", width=12, command=find_password)
search.grid(column=3, row=1)

mainloop()
