from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please enter all fields")
    else:
        try:
            # Prøv at åbne datafilen og læs eksisterende data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Læs eksisterende data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # Hvis filen ikke findes, opretter vi den med ny data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)  # Gemmer ny data
        else:
            # Hvis filen findes, opdater eksisterende data med ny data
            data.update(new_data)

            # Skriv den opdaterede data til filen
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Ryd inputfelterne
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- search password ------------------------------- #
def search_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo("Error", "No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo("website", f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo("Error", f"There are no details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#website label
website_label = Label(window, text="Website:")
website_label.grid(column=0, row=1)

#website entry
website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky=EW)

#email/username label
email_label = Label(window, text="Email/Username:")
email_label.grid(column=0, row=2)

#email/username entry
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky=EW)

#password label
password_label = Label(window, text="Password:")
password_label.grid(column=0, row=3)

#password generator entry?
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky=EW)

#generate button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky=EW)

#search button
search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1, sticky=EW)

#Add button
add_button=Button(window, text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

window.mainloop()