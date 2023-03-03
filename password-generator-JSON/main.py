from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    pwd_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = web_input.get()
    email = email_input.get()
    pwd = pwd_input.get()
    new_data = {
        website: {
            "email:": email,
            "password: ": pwd,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web_input.get(),
                                       message=f"These are the details entered:\nWebsite: {website}\nEmail: {email}\nPassword: {pwd}\nIs it okay to save?")
        if is_ok:
            try:
                with open("passwords.json", "r") as data_file:
                    # reading file
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("passwords.json", "w") as data_file:
                    # writing into file
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating file data
                data.update(new_data)
                with open("passwords.json", "w") as data_file:
                    # writing into file
                    json.dump(data, data_file, indent=4)
            finally:
                web_input.delete(0, 'end')
                pwd_input.delete(0, 'end')
                web_input.focus()


# ------------------------FIND PASSWORD -------------------------------#

def find_password():
    website = web_input.get()
    try:
        with open("passwords.json", "r") as data_file:
            # reading file
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File does not exist", message="There is no data yet.")
    else:
        try:
            return_data = data[website]
        except KeyError:
            messagebox.showinfo(title="Password does not exist", message="Add a password for this website.")
        else:
            email = return_data['email:']
            password = return_data['password: ']
            messagebox.showinfo(title=f"Email/Password for {website}", message=f"Email: {email}\nPassword: {password}")
        finally:
            pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

web_input = Entry(width=20)
web_input.grid(row=1, column=1)
web_input.focus()

email_input = Entry(width=20)
email_input.grid(row=2, column=1)
email_input.insert(0, "noaswim89@gmail.com")

pwd_input = Entry(width=20)
pwd_input.grid(row=3, column=1)

generate_button = Button(text="Generate password", command=generate, borderwidth=0)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=add, borderwidth=0, width=36)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=find_password, borderwidth=0, width=13)
search_button.grid(row=1, column=2)

window.mainloop()
