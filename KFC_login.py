from tkinter import Tk, PhotoImage, Label, Button, Entry, Frame, LabelFrame, messagebox, Radiobutton, Checkbutton
import os
from PIL import ImageTk
import webbrowser
from base import Database

db = Database()
window = Tk()
window.title("KFC Uzbekistan")
window.configure(bg="darkred")

image_icon = PhotoImage(file="Image(KFC)/logo2.png")
window.iconphoto(True, image_icon)

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
center_x = int(width / 2 - 1125 / 2)
center_y = int(height / 2 - 600 / 2)
window.geometry(f"{1125}x{600}+{center_x}+{center_y}")

# BG = ImageTk.PhotoImage(file="Image(KFC)/bg.jpg")
# bg_label = Label(window, image=BG)
# bg_label.grid()

# -------------------------------------------------------------------------------------

yt_logo = ImageTk.PhotoImage(file="Image(KFC)/yt_logo.png")
KFC = ImageTk.PhotoImage(file="Image(KFC)/kfc.png")
photo = ImageTk.PhotoImage(file="Image(KFC)/logo2.png")

bg_label_logo = Label(window, image=KFC, bg="darkred")
bg_label_logo.place(x=400, y=190)


# -------------------------------------------------------------------------------------

# ad = Label(window)
# ad.place(x=900, y=190)
# player = tkvideo("kfc(1)", label=ad, loop=1, size=(300, 250))
# player.play()


def login():
    username = entry_username.get()
    password = entry_password.get()
    user = db.login_user(username=username.lower(), password=password)
    if user:
        messagebox.showinfo(title="Success",
                            message="Successfully login")
        window.destroy()
        os.system("python KFC_ordering.py")
    else:
        messagebox.showerror(title="Error",
                             message="Invalid login")


def open_online_kfc():
    webbrowser.open_new("https://www.kfc.com.uz/")


def open_youtube():
    webbrowser.open_new("https://www.youtube.com/@kfc")


def register():
    window.destroy()
    os.system("python KFC_register.py")


kfc = Label(window, image=photo)
kfc.place(x=880, y=500)

text = Button(window, text="Online KFC", font=("calibri", 18, "bold"), command=open_online_kfc, padx=35)
text.place(x=930, y=500)

# =======================================================================================

yt = Label(window, image=yt_logo)
yt.place(x=880, y=550)

text1 = Button(window, text="YouTube Channel", font=("calibri", 18, "bold"), command=open_youtube)
text1.place(x=930, y=550)


# ----------------------------------------------------------------------------------------


def show():
    if entry_password.cget("show") == "*":
        entry_password.config(show="")
    else:
        entry_password.config(show="*")


frame = Frame(window, bg="#BD1719")
frame.grid(pady=150, padx=50)

label_frame = LabelFrame(frame, bg="#BD1719")
label_frame.grid()

# -------------------------------------------------------------------------------------------------------------

checkbutton = Checkbutton(label_frame, text="Show password", bg="#BD1719", fg="white", activeforeground="White", activebackground="darkred", font=8, command=show)
checkbutton.grid(row=4, column=0, sticky="W")

label_username = Label(label_frame, text="Username: ", font=('calibri', 20, "bold"), bg="#BD1719", fg="lightgray")
label_username.grid(row=0, column=0, sticky="W")

entry_username = Entry(label_frame, width=25, font=("calibri", 15, "bold"))
entry_username.grid(row=1, column=0, ipady=5, sticky="W")

label_password = Label(label_frame, text="Password: ", font=('calibri', 20, "bold"), bg="#BD1719", fg="lightgray")
label_password.grid(row=2, column=0, sticky="W")

entry_password = Entry(label_frame, width=25, font=("calibri", 15, "bold"), show="*")
entry_password.grid(row=3, column=0, ipady=5, sticky="W")

login_button = Button(label_frame, text="Login", width=35, font=("calibri", 15, "bold"), command=login)
login_button.grid(row=5, column=0, sticky="W")

register_button = Button(label_frame, text="Register", width=35, font=("calibri", 15, "bold"), command=register)
register_button.grid(row=6, column=0, sticky="W")

for widget in label_frame.winfo_children():
    widget.grid_configure(padx=8, pady=5)

window.mainloop()
