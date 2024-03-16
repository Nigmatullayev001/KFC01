from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk
from base import Database

windows = Tk()
windows.title("KFC Uzbekistan")
windows.configure(bg="darkred")
image_icon = PhotoImage(file="Image(KFC)/logo2.png")
windows.iconphoto(True, image_icon)
db = Database()

bg2 = ImageTk.PhotoImage(file="Image(KFC)/kfc_PNG7.png")
bg3 = ImageTk.PhotoImage(file="Image(KFC)/png-kfc.png")

width = windows.winfo_screenwidth()
height = windows.winfo_screenheight()
center_x = int(width / 2 - 1125 / 2)
center_y = int(height / 2 - 600 / 2)
windows.geometry(f"{1125}x{600}+{center_x}+{center_y}")

bg = Label(windows, image=bg2, bg="darkred")
bg.place(x=500, y=350)

bg1 = Label(windows, image=bg3, bg="darkred")
bg1.place(x=500, y=-10)


# def get_id():
# num = 1
# for u_id in user_id[]:
#     d =u_id
# if num != 0:
#     user_a = d[0]
#     num -= 1


def login_open():
    windows.destroy()
    os.system("python KFC_login.py")


def register():
    username = username_entry.get()
    username1 = len(username)
    password = password_entry.get()
    password1 = len(password)
    email = email_entry.get()
    email1 = len(email)
    age = age_entry.get()
    phone_number = phone_entry.get()
    phone_number1 = len(phone_number)
    normal_num = len("+998(--)--- -- --")
    normal_num1 = len("+998121231212")
    if username1 >= 2 and password1 >= 6 and phone_number1 == normal_num or normal_num1 and email1 >= 11:

        messagebox.showinfo(title="Success!",
                            message="Successfully Registered")
        db.insert_user(username=username.lower(), password=password, email=email, age=age, phone_number=phone_number)
        user_id = db.read_all_user()[-1]
        messagebox.showwarning(title="Warning!", message=f"Remember alert id!!\n Your ID is {user_id[0]}")

        login_open()
    else:
        messagebox.showerror(title="ERROR!",
                             message="Nimadir xato ketgan iltimos yana bir marotava urunib ko'ring!")


frame = Frame(windows, bg="darkred")
frame.grid(padx=60, pady=45)

user_frame = LabelFrame(frame, bg="darkred")
user_frame.grid(row=0, column=0, padx=30, pady=30)

username_label = Label(user_frame, bg="darkred",
                       text="Username",
                       fg="White",
                       font=("gill sans", 12))
username_label.grid(row=1, column=0, sticky="W")
username_entry = Entry(user_frame, bg="White")
username_entry.grid(row=2, column=0, ipady=5, sticky="news")

password_label = Label(user_frame, bg="darkred",
                       text="Password (6ta elementdan ko'piroq bo'lsin)",
                       fg="White",
                       font=("gill sans", 12))
password_label.grid(row=3, column=0, sticky="W")
password_entry = Entry(user_frame, bg="White")
password_entry.grid(row=4, column=0, ipady=5, sticky="news")

email_label = Label(user_frame, bg="darkred",
                    text="Email",
                    fg="White",
                    font=("gill sans", 12))
email_label.grid(row=5, column=0, sticky="W")
email_entry = Entry(user_frame, bg="White", width=45)
email_entry.grid(row=6, column=0, ipady=5, columnspan=2, sticky="news")

age_label = Label(user_frame, bg="darkred",
                  text="Age (majburiy emas)",
                  fg="White",
                  font=("gill sans", 12))
age_label.grid(row=7, column=0, sticky="W")
age_entry = Spinbox(user_frame, bg="White", from_=0, to=99)
age_entry.grid(row=8, column=0, ipady=5, sticky="news")

phone_label = Label(user_frame, bg="darkred",
                    text="Phone Number",
                    fg="White",
                    font=("gill sans", 12))
phone_label.grid(row=9, column=0, sticky="W")
phone_entry = Entry(user_frame, bg="White")
phone_entry.grid(row=10, column=0, ipady=5, sticky="news")

phone_entry.insert(1, "+998")
email_entry.insert(-1, "@gmail.com")

button = Button(user_frame,
                text="Register",
                fg="BLACK",
                font=("gill sans", 12, "bold"),
                command=register)
button.grid(row=11, column=0, columnspan=2, sticky="news")

back = Button(windows, text="<-- BACK", font=("calibri", 13, "bold"), width=10, command=login_open)
back.place(x=10, y=550)

for widget in user_frame.winfo_children():
    widget.grid_configure(padx=8, pady=5)

windows.mainloop()
