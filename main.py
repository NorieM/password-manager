from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from generator import Generate


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_password():
    generator = Generate()
    password = generator.generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# save password to data.json
def save_password():
    # get data to be saved
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:
                    {'email': email,
                     'password': password
                     }
                }

    if website and password and email:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showwarning(message='Please enter missing details!', title='Missing details')


# ---------------------------- FIND WEBSITE ------------------------------- #

def find_website():
    website = website_entry.get()
    if not website:
        return
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(message='No saved passwords!', title="No passwords")
    else:
        if website in data:
            details = data[website]
            email = details['email']
            password = details['password']
            messagebox.showinfo(message=f'Username: {email}\nPassword: {password}', title=f'Details for {website}')
        else:
            messagebox.showwarning(message=f'Details not found for {website}!', title='Not found')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.resizable(False, False)
window.config(padx=10, pady=20, bg='white')

logo = PhotoImage(file='logo.png')

window.iconphoto(False, logo)

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.create_image(100, 100, image=logo)

canvas.grid(row=0, column=1)

website_label = Label(text='Website:', bg='white')
website_label.grid(row=1, column=0, sticky=E)

email_label = Label(text='Email/Username:', bg='white')
email_label.grid(row=2, column=0, sticky=E)

password_label = Label(text='Password:', bg='white')
password_label.grid(row=3, column=0, sticky=E)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=EW)

generate_password = Button(text='Generate Password', width=21, bg='white', command=get_password)
generate_password.grid(row=3, column=2, sticky=EW)

add_password = Button(text='Add', width=36, bg='white', command=save_password)
add_password.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text='Search', width=21, bg='light blue', command=find_website)
search_button.grid(row=1, column=2)

website_entry.focus()
email_entry.insert(0, 'norie.macewan@tiscali.co.uk')

window.mainloop()
