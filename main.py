from tkinter import *

root = Tk()
root.geometry("1600x1600")
root.title("IDK")

label1 = Label(root, text="")

def one():
    label1["text"] = "Rohith Has Been Alloted to the Universe"

btn1 = Button(root, text="Show Hospital!!!!", command=one)
btn1.place(anchor=CENTER, relx=0.5, rely=0.1)
label1.place(anchor=CENTER, relx=0.5, rely=0.15)

label2 = Label(root, text="")

def two():
    label2["text"] = "He Works In Rohith's Tech"

btn2 = Button(root, text="Show His IT Company", command=two)
btn2.place(anchor=CENTER, relx=0.5, rely=0.25)
label2.place(anchor=CENTER, relx=0.5, rely=0.3)

label3 = Label(root, text="")

def three():
    label3["text"] = "He Is In NASA"

btn3 = Button(root, text="Show His Science Company", command=three)
btn3.place(anchor=CENTER, relx=0.5, rely=0.4)
label3.place(anchor=CENTER, relx=0.5, rely=0.45)

root.mainloop()