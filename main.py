from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    password_entry.delete(0, END)

    letters = list(map(chr, range(97, 123)))
    letters = letters + list(map(lambda ch: ch.upper(), letters))
    numbers = [str(i) for i in range(10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# save password to data.txt
def save_password():
    # get data to be saved
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website and password and email:
        # confirm info with user
        message = f'Save these details?\n\nEmail: {email}\nPassword: {password}'
        confirm = messagebox.askokcancel(message=message, title=f'{website}')

        # if user confirms save details and reser form
        if confirm:
            with open('data.txt', 'a+') as data_file:
                info = [website, email, password]
                data_file.write(','.join(info) + '\n')
                messagebox.showinfo(message=f'Credentials saved for {website}!', title='Saved')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showwarning(message='Please enter missing details!', title='Missing details')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.resizable(False,False)
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

generate_password = Button(text='Generate Password', width=36, bg='white', command=generate_password)
generate_password.grid(row=3, column=2, sticky=EW)

add_password = Button(text='Add', width=36, bg='white', command=save_password)
add_password.grid(row=4, column=1, columnspan=2, sticky="EW")

website_entry.focus()
email_entry.insert(0, 'norie.macewan@tiscali.co.uk')

window.mainloop()
