from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for letter in range(randint(8,10))]
    symbol_list = [choice(symbols) for symbol in range(randint(2, 4))]
    number_list = [choice(numbers) for number in range(randint(2,4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save_password():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": user,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops", message = "Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            # saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(first = 0, last= END)
            password_entry.delete(first = 0, last = END)
            
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title = f"{website}", message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title = "Info", message = f"No details for the {website} exist")


        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)

canvas = Canvas(width = 200, height = 200)
logo_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_image)
canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)
user_label = Label(text = "Email/Username:")
user_label.grid(row = 2, column = 0)
password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)

website_entry = Entry(width = 30)
website_entry.grid(row = 1, column = 1, sticky = "W")
website_entry.focus()
user_entry = Entry(width = 35)
user_entry.grid(row = 2, column = 1, columnspan = 2, sticky = "EW")
user_entry.insert(0, "dusan_vojnovic@yahoo.com")
password_entry = Entry(width = 30)
password_entry.grid(row = 3, column = 1, sticky = "W")

generate_button = Button(text = "Generate Password", command = generate_password)
generate_button.grid(row = 3, column = 2, sticky = "EW")
add_button = Button(text = "Add", width = 36, command = save_password)
add_button.grid(row = 4, column = 1, columnspan = 2, sticky = "EW")
search_button = Button(text = "Search", command = find_password)
search_button.grid(row = 1, column = 2, sticky = "EW")


window.mainloop()