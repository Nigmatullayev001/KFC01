import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkvideo import tkvideo
from base import Database

# fd = Food_order()
db = Database()
window = Tk()
window.title("KFC Uzbekistan")
window.configure(bg="darkred")

image_icon = PhotoImage(file="Image(KFC)/logo2.png")
window.iconphoto(True, image_icon)
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
center_x = int(width / 2 - 1180 / 2)
center_y = int(height / 2 - 600 / 2)
window.geometry(f"{1180}x{600}+{center_x}+{center_y}")

Lb = Listbox(window, bg="Darkred", fg="white", font=8)
food = ""


def burger():
    global bu
    messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")
    db.insert_food("Chickburger", " 35_000", "1", "35_000")


def coffee():
    global co
    messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")
    db.insert_food("Coffee 0.4l", "17_000", "1", "17_000")


def chiken_nugets():
    global ch
    messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")
    db.insert_food("To'vuq oyoqchalari", "35_000", "1", "35_000")


def choy():
    global cho
    messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")
    db.insert_food("Ko'k choy", "7_000", "1", "7_000")


def longer():
    global lo
    messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")
    db.insert_food("Longer", "15_000", "1", '15_000')


def buy():
    lb = Lb
    if lb:
        messagebox.showinfo(title="ORDER accepted!", message="ORDER accepted!!!")
        Lb.delete(0, END)
    else:
        messagebox.showerror(title="ERROR", message="Please put fast food in the cart!")


Lb.place(y=200, x=950)


def delete_item():
    Lb.delete(ANCHOR)


#
# delete_button = Button(windows, text="DELETE ITEM", font=8, width=15, command=delete_item)
# delete_button.grid(row=1, column=0, sticky="E")
# def burger2():
#     fd.burger()
#     messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")
#
#
# def coffees():
#     fd.coffee()
#     messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")
#
#
# def chiken_nugets()():
#     fd.chiken_nugets()_nugets()
#     messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")
#
#
# def choy2():
#     fd.choy()
#     messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")
#
#
# def longers():
#     fd.longer()
#     messagebox.showinfo(title="", message="Your order has been sent to the 'basket' page")


menu = ImageTk.PhotoImage(file="Image(KFC)/menu.png")
ad_frame = Frame(window)
ad_frame.grid(row=1, column=0, padx=15, pady=15)

ad_label_frame = LabelFrame(ad_frame)
ad_label_frame.grid()

ads1 = Label(ad_label_frame, text="AD", font=10)
ads1.pack()
ad1 = Label(ad_label_frame)
ad1.pack()
player1 = tkvideo("Image(KFC)/kfc (1).mp4", label=ad1, loop=10, size=(200, 100))
player1.play()

ads2 = Label(ad_label_frame, text="AD", font=10)
ads2.pack()
ad2 = Label(ad_label_frame)
ad2.pack()
player2 = tkvideo("Image(KFC)/kfc (2).mp4", label=ad2, loop=10, size=(200, 100))
player2.play()

ads3 = Label(ad_label_frame, text="AD", font=10)
ads3.pack()
ad3 = Label(ad_label_frame)
ad3.pack()
player3 = tkvideo("Image(KFC)/kfc (3).mp4", label=ad3, loop=10, size=(200, 100))
player3.play()

bg = ImageTk.PhotoImage(file="Image(KFC)/images-removebg-preview.png")

kfc1 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (1).jpg")
kfc2 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (2).jpg")
kfc3 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (3).jpg")
kfc4 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (4).jpg")
kfc5 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (5).jpg")
kfc6 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (6).jpg")
kfc7 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (20).jpg")
kfc21 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (21).jpg")

# ===================================================================================

kfc8 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (7).jpg")
kfc9 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (8).jpg")
kfc10 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (9).jpg")
kfc11 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (10).jpg")
kfc12 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (11).jpg")

# =====================================================================================

kfc13 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (12).jpg")
kfc14 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (13).jpg")
kfc15 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (14).jpg")
kfc16 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (15).jpg")
kfc17 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (16).jpg")
kfc18 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (17).jpg")
kfc19 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (18).jpg")
kfc20 = ImageTk.PhotoImage(file="Image(KFC)/kfc_menu/kfc_menu (19).jpg")

# ================================================================================

frame = Frame(window)
frame.place(x=250, y=200)

labelframe = LabelFrame(frame, bg="darkred")
labelframe.grid()

logo_label = Label(window, image=bg, bg="darkred")
logo_label.place(x=300, y=5)

photo1 = Label(labelframe, image=kfc1)
photo1.grid(row=0, column=0, padx=8, pady=8)
photo2 = Label(labelframe, image=kfc8)
photo2.grid(row=0, column=1, padx=8, pady=8)
photo3 = Label(labelframe, image=kfc19)
photo3.grid(row=0, column=2, padx=8, pady=8)
photo4 = Label(labelframe, image=kfc20)
photo4.grid(row=0, column=3, padx=8, pady=8)
photo5 = Label(labelframe, image=kfc21)
photo5.grid(row=1, column=0, padx=8, pady=8)
photo6 = Label(labelframe, image=kfc4)
photo6.grid(row=1, column=1, padx=8, pady=8)
photo7 = Label(labelframe, image=kfc2)
photo7.grid(row=1, column=2, padx=8, pady=8)
photo8 = Label(labelframe, image=kfc10)
photo8.grid(row=1, column=3, padx=8, pady=8)

price1 = Label(window)
price2 = Label(window)
price3 = Label(window)
price4 = Label(window)
price5 = Label(window)
price6 = Label(window)
price7 = Label(window)
price8 = Label(window)
price9 = Label(window)
price10 = Label(window)
price11 = Label(window)
price12 = Label(window)


class Foods:
    def __init__(self, name, price, how_much, total):
        self.name = name
        self.price = price
        self.how_much = how_much
        self.total = total


def basket():
    window.destroy()
    os.system("python basket_kfc.py")


def log_out():
    window.destroy()
    os.system("python KFC_login.py")


lb_frame = Frame(window)
lb_frame.place(x=950, y=200)

lb_label_frame = LabelFrame(lb_frame)
lb_label_frame.grid()


def drinks():
    global price9
    global price10
    global price11
    global price12
    global photo9
    global photo10
    global photo11
    global photo12
    global button10
    global button11
    global button12
    global button9

    delete_label()
    photo9 = Label(labelframe, image=kfc8)
    photo9.grid(row=0, column=0, padx=8, pady=8)
    photo10 = Label(labelframe, image=kfc10)
    photo10.grid(row=0, column=1, padx=8, pady=8)
    photo11 = Label(labelframe, image=kfc9)
    photo11.grid(row=0, column=2, padx=8, pady=8)
    photo12 = Label(labelframe, image=kfc11)
    photo12.grid(row=0, column=3, padx=8, pady=8)

    price9 = Label(labelframe, text="Coffee 0.4L\n \n17.000 so'm", font=8, fg="white", bg="darkred")
    price9.grid(row=1, column=0, padx=8, pady=8)
    button9 = Button(labelframe, text="Savatga solish", font="bold", command=coffee)
    button9.grid(row=2, column=0)

    price10 = Label(labelframe, text="Coffee 0.3L \n15.000 so'm", font=8, fg="white", bg="darkred")
    price10.grid(row=1, column=1, padx=8, pady=8)
    button10 = Button(labelframe, text="Savatga solish", font="bold", command=coffee)
    button10.grid(row=2, column=1)

    price11 = Label(labelframe, text="Coffee 0.2L \n12.000 so'm", font=8, fg="white", bg="darkred")
    price11.grid(row=1, column=2, padx=8, pady=8)
    button11 = Button(labelframe, text="Savatga solish", font="bold", command=coffee)
    button11.grid(row=2, column=2)

    price12 = Label(labelframe, text="Ko'k Choy \n6.000 so'm", font=8, fg="white", bg="darkred")
    price12.grid(row=1, column=3, padx=8, pady=8)
    button12 = Button(labelframe, text="Savatga solish", font="bold", command=choy)
    button12.grid(row=2, column=3)


def burgers():
    global price5
    global price6
    global price7
    global price8
    global photo5
    global photo6
    global photo7
    global photo8
    global button5
    global button6
    global button7
    global button8

    delete_label()
    photo5 = Label(labelframe, image=kfc14)
    photo5.grid(row=0, column=0, padx=8, pady=8)
    photo6 = Label(labelframe, image=kfc15)
    photo6.grid(row=0, column=1, padx=8, pady=8)
    photo7 = Label(labelframe, image=kfc19)
    photo7.grid(row=0, column=2, padx=8, pady=8)
    photo8 = Label(labelframe, image=kfc20)
    photo8.grid(row=0, column=3, padx=8, pady=8)

    button5 = Button(labelframe, text="Savatga solish", font="bold", command=burger)
    button5.grid(row=2, column=0)

    button6 = Button(labelframe, text="Savatga solish", font="bold", command=burger)
    button6.grid(row=2, column=1)

    button7 = Button(labelframe, text="Savatga solish", font="bold", command=burger)
    button7.grid(row=2, column=2)

    button8 = Button(labelframe, text="Savatga solish", font="bold", command=longer)
    button8.grid(row=2, column=3)

    price5 = Label(labelframe, text="Chickburger \n35.000 so'm", font=8, fg="white", bg="darkred")
    price5.grid(row=1, column=0, padx=8, pady=8)
    price6 = Label(labelframe, text="Medium Chickburger \n27.000 so'm", font=8, fg="white", bg="darkred")
    price6.grid(row=1, column=1, padx=8, pady=8)
    price7 = Label(labelframe, text="Small chickburger \n20.000 so'm", font=8, fg="white", bg="darkred")
    price7.grid(row=1, column=2, padx=8, pady=8)
    price8 = Label(labelframe, text="Longer \n15.000 so'm", font=8, fg="white", bg="darkred")
    price8.grid(row=1, column=3, padx=8, pady=8)


def main_menu():
    global price1
    global price2
    global price3
    global price4
    global photo1
    global photo2
    global photo3
    global photo4
    global button1
    global button2
    global button3
    global button4

    delete_label()
    photo1 = Label(labelframe, image=kfc1)
    photo1.grid(row=0, column=0, padx=8, pady=8)
    photo2 = Label(labelframe, image=kfc8)
    photo2.grid(row=0, column=1, padx=8, pady=8)
    photo3 = Label(labelframe, image=kfc19)
    photo3.grid(row=0, column=2, padx=8, pady=8)
    photo4 = Label(labelframe, image=kfc20)
    photo4.grid(row=0, column=3, padx=8, pady=8)

    price1 = Label(labelframe, text="To'vuq oyoqchalari \n18ta \n37.000 so'm", font=8, fg="white", bg="darkred")
    price1.grid(row=1, column=0, padx=8, pady=8)
    button1 = Button(labelframe, text="Savatga solish", font="bold", command=chiken_nugets)
    button1.grid(row=2, column=0)

    price2 = Label(labelframe, text="Coffee 0.4l \n17.000 so'm", font=8, fg="white", bg="darkred")
    price2.grid(row=1, column=1, padx=8, pady=8)
    button2 = Button(labelframe, text="Savatga solish", font="bold", command=coffee)
    button2.grid(row=2, column=1)

    price3 = Label(labelframe, text="Big sanders burger \n37.000 so'm", font=8, fg="white", bg="darkred")
    price3.grid(row=1, column=2, padx=8, pady=8)
    button3 = Button(labelframe, text="Savatga solish", font="bold", command=burger)
    button3.grid(row=2, column=2)

    price4 = Label(labelframe, text="Longer \n15.000 so'm", font=8, fg="white", bg="darkred")
    price4.grid(row=1, column=3, padx=8, pady=8)
    button4 = Button(labelframe, text="Savatga solish", font="bold", command=longer)
    button4.grid(row=2, column=3)


def buckets():
    global price13
    global price14
    global price15
    global price16
    global photo13
    global photo14
    global photo15
    global photo16
    global button13
    global button14
    global button15
    global button16

    delete_label()
    photo13 = Label(labelframe, image=kfc1)
    photo13.grid(row=0, column=0, padx=8, pady=8)
    photo14 = Label(labelframe, image=kfc2)
    photo14.grid(row=0, column=1, padx=8, pady=8)
    photo15 = Label(labelframe, image=kfc3)
    photo15.grid(row=0, column=2, padx=8, pady=8)
    photo16 = Label(labelframe, image=kfc21)
    photo16.grid(row=0, column=3, padx=8, pady=8)

    price13 = Label(labelframe, text="To'vuq oyoqchalari \n18ta \n37.000 so'm", font=8, fg="white", bg="darkred")
    price13.grid(row=1, column=0, padx=8, pady=8)
    button13 = Button(labelframe, text="Savatga solish", font="bold", command=chiken_nugets)
    button13.grid(row=2, column=0)

    price14 = Label(labelframe, text="Coffee 0.4l \n17.000 so'm", font=8, fg="white", bg="darkred")
    price14.grid(row=1, column=1, padx=8, pady=8)
    button14 = Button(labelframe, text="Savatga solish", font="bold", command=chiken_nugets)
    button14.grid(row=2, column=1)

    price15 = Label(labelframe, text="Big sanders burger \n37.000 so'm", font=8, fg="white", bg="darkred")
    price15.grid(row=1, column=2, padx=8, pady=8)
    button15 = Button(labelframe, text="Savatga solish", font="bold", command=chiken_nugets)
    button15.grid(row=2, column=2)

    price16 = Label(labelframe, text="Longer \n15.000 so'm", font=8, fg="white", bg="darkred")
    price16.grid(row=1, column=3, padx=8, pady=8)
    button16 = Button(labelframe, text="Savatga solish", font="bold", command=chiken_nugets)
    button16.grid(row=2, column=3)


def delete_all():
    price1.destroy()
    price2.destroy()
    price3.destroy()
    price4.destroy()
    price5.destroy()
    price6.destroy()
    price7.destroy()
    price8.destroy()
    price9.destroy()
    price10.destroy()
    price11.destroy()
    price12.destroy()
    price13.destroy()
    price14.destroy()
    price15.destroy()
    price16.destroy()
    photo1.destroy()
    photo2.destroy()
    photo3.destroy()
    photo4.destroy()
    photo5.destroy()
    photo6.destroy()
    photo7.destroy()
    photo8.destroy()
    photo9.destroy()
    photo10.destroy()
    photo11.destroy()
    photo12.destroy()
    photo13.destroy()
    photo14.destroy()
    photo15.destroy()
    photo15.destroy()
    ad1.destroy()
    ads1.destroy()
    ad2.destroy()
    ads2.destroy()
    ad3.destroy()
    ads3.destroy()
    frame.destroy()
    labelframe.destroy()
    logo_label.destroy()
    labelframe.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    button11.destroy()
    button12.destroy()
    button13.destroy()
    button14.destroy()
    button15.destroy()
    button16.destroy()


def delete_label():
    price1.destroy()
    price2.destroy()
    price3.destroy()
    price4.destroy()
    price5.destroy()
    price6.destroy()
    price7.destroy()
    price8.destroy()
    price9.destroy()
    price10.destroy()
    price11.destroy()
    price12.destroy()
    photo1.destroy()
    photo2.destroy()
    photo3.destroy()
    photo4.destroy()
    photo5.destroy()
    photo6.destroy()
    photo7.destroy()
    photo8.destroy()


def profile():
    window.destroy()
    os.system("python KFC_profile.py")


def about():
    messagebox.showinfo(title="About",
                        message=f"Company name: KFC Uzbekistan,\nOwner: SVS\nLaunch date: 11/03/2024\nSite type: Fast food")


menubutton = Menubutton(window,
                        image=menu,
                        relief=RAISED,
                        bg="darkred",
                        activebackground="darkred")

menubutton.grid(row=0, column=0, sticky="W")
menubutton.menu = Menu(menubutton, tearoff=0)
menubutton["menu"] = menubutton.menu
menubutton.menu.add_command(label="Main Menu", font=("calibri", 25, "bold"), command=main_menu)
menubutton.menu.add_command(label="Burgers", font=("calibri", 25, "bold"), command=burgers)
menubutton.menu.add_command(label="Drinks", font=("calibri", 25, "bold"), command=drinks)
menubutton.menu.add_command(label="Buckets", font=("calibri", 25, "bold"), command=buckets)
menubutton.menu.add_command(label="Menus", font=("calibri", 25, "bold"))
menubutton.menu.add_command(label="Basket", font=("calibri", 25, "bold"), command=basket)
menubutton.menu.add_command(label="About Us", font=("calibri", 25, "bold"), command=about)
menubutton.menu.add_command(label="Profile", font=("calibri", 25, "bold"), command=profile)

log_out = Button(window, text="Logout", font=8, command=log_out)
log_out.place(x=1100, y=5)

for widget in labelframe.winfo_children():
    widget.grid_configure(padx=8, pady=8)

window.mainloop()
