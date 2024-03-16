import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from base import Database

db = Database()
a = db.read_all_user()

window = Tk()

image_icon = PhotoImage(file="Image(KFC)/logo2.png")
window.iconphoto(True, image_icon)

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
center_x = int(width / 2 - 500 / 2)
center_y = int(height / 2 - 200 / 2)
window.geometry(f"{500}x{200}+{center_x}+{center_y}")
window.title("KFC Uzbekistan")
window.configure(bg="darkred")

entry = Entry(window, font=8)
entry.grid(row=0, column=0, pady=8, padx=10)

for aa in a:
    text = aa[0]
    text2 = aa[1]
    text3 = aa[2]
    text4 = aa[3]
    ad = f"ID: {text} \nUsername: {text2} \nPassword: ****** \n Email: {[text4]}"

label_username = Label(window, text=ad, bg="darkred", fg="White", font=9)
label_username.place(x=15, y=100)


def log_in():
    window.destroy()
    os.system("python KFC_login.py")


def delete_user():
    if ad:
        id_u = entry.get()
        db.delete_user(id=id_u, )
        entry.delete(0, END)
        messagebox.showinfo(title="Deleted", message="Xisob o'chirildi")
        log_in()
    else:
        messagebox.showerror(title="ERROR", message="bunday xisob bazada yo'q")


def back():
    window.destroy()
    os.system("python KFC_ordering.py")


back_button = Button(window, text="<--", font=("calibri", 8, "bold"), width=10, command=back)
back_button.grid(row=0, column=1, sticky="W")

button = Button(window, text="Delete", command=delete_user)
button.grid(row=1, column=0, pady=8, padx=10, sticky="news")

window.mainloop()
