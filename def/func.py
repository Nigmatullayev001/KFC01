from tkinter import *

from PIL import ImageTk

window = Tk()

bg = ImageTk.PhotoImage(file="Image(KFC)/bg2.png")

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

# 404 Error

frame = Frame(window)
frame.place(x=250, y=200)

labelframe = LabelFrame(frame, bg="darkred")
labelframe.grid()

logo_label = Label(window, image=bg, bg="darkred")
logo_label.grid(row=0, column=1)


photo1 = Label(labelframe, image=kfc1)
photo1.grid(row=0, column=0, padx=8, pady=8)
photo2 = Label(labelframe, image=kfc8)
photo2.grid(row=0, column=1, padx=8, pady=8)
photo3 = Label(labelframe, image=kfc19)
photo3.grid(row=0, column=2, padx=8, pady=8)
photo4 = Label(labelframe, image=kfc20)
photo4.grid(row=0, column=3, padx=8, pady=8)

price1 = Label(labelframe, text="To'vuq oyoqchalari \n18ta \n35.000 so'm", font=8, fg="white", bg="darkred")
price1.grid(row=1, column=0, padx=8, pady=8)
button1 = Button(labelframe, text="Savatga solish", font="bold", command="basket")
button1.grid(row=2, column=0)

price2 = Label(labelframe, text="Coffee 0.4l \n17.000 so'm", font=8, fg="white", bg="darkred")
price2.grid(row=1, column=1, padx=8, pady=8)
button2 = Button(labelframe, text="Savatga solish", font="bold", command="basket")
button2.grid(row=2, column=1)

price3 = Label(labelframe, text="Big sanders burger \n37.000 so'm", font=8, fg="white", bg="darkred")
price3.grid(row=1, column=2, padx=8, pady=8)
button3 = Button(labelframe, text="Savatga solish", font="bold", command="basket")
button3.grid(row=2, column=2)

price4 = Label(labelframe, text="Longer \n15.000 so'm", font=8, fg="white", bg="darkred")
price4.grid(row=1, column=3, padx=8, pady=8)
button4 = Button(labelframe, text="Savatga solish", font="bold", command="basket")
button4.grid(row=2, column=3)
