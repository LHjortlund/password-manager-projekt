from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    with open("data.text", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)

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
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky=EW)

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
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, sticky=EW)

#Add button
add_button=Button(window, text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

window.mainloop()