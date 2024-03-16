import os
from tkinter import *
from tkinter import messagebox
from base import Database

db = Database()
window = Tk()
window.title("KFC Uzbekistan")
window.configure(bg="darkred")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
center_x = int(width / 2 - 550 / 2)
center_y = int(height / 2 - 300 / 2)
window.geometry(f"{550}x{300}+{center_x}+{center_y}")
image_icon = PhotoImage(file="Image(KFC)/logo2.png")
window.iconphoto(True, image_icon)

Lb = Listbox(window, bg="Darkred", fg="white", font=8, width=50)
food = ""




def burger():
    global bu
    bu = Lb.insert(-1, "Chickburger, price=35.000, how_much=1, total=35.000")
    db.insert_food("Chickburger", " 35_000", "1", "35_000")

def coffee():
    global co
    co = Lb.insert(-1, "Coffee 0.4l, price 17.000, how_much=1,  total 17.000")
    db.insert_food("Coffee 0.4l", "17_000", "1", "17_000")

def chicken_nugets():
    global ch
    ch = Lb.insert(-1, "To'vuq oyoqchalari, price 35.000, how_much 1, total 35.000")
    db.insert_food("To'vuq oyoqchalari", "35_000", "1", "35_000")

def choy():
    global cho
    cho = Lb.insert(-1, "Ko'k choy, price 7.000, how_much=1, total 7.000")
    db.insert_food("Ko'k choy", "7_000", "1", "7_000")

def longer():
    global lo
    lo = Lb.insert(-1, "Longer, price 15.000, how_much=1, total 15.000")
    db.insert_food("Longer", "15_000", "1", '15_000')


def buy():
    lb = Lb
    if lb:
        messagebox.showinfo(title="ORDER accepted!", message="ORDER accepted!!!")
        Lb.delete(0, END)
    else:
        messagebox.showerror(title="ERROR", message="Please put fast food in the cart!")


Lb.grid(row=0, column=0)


def delete_item():
    Lb.delete(ANCHOR)


def back():
    window.destroy()
    os.system("python KFC_ordering.py")


delete_button = Button(window, text="DELETE ITEM", font=8, width=15, command=delete_item)
delete_button.grid(row=1, column=0, sticky="E")

buy_button = Button(window, text="B U Y", font=8, width=15, command=buy)
buy_button.grid(row=1, column=0, sticky="N")

back_button = Button(window, text="<--", font=("calibri", 15, "bold"), width=15, command=back)
back_button.grid(row=1, column=0, sticky="W")

window.mainloop()
