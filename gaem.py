#Libraries
from tkinter import *
import random 

#Root Window GUI
window=Tk()
window.title("Color Randomizer Game")
window.configure(bg="white")

#Label
color_label = Label(window,bg="white",font=("inter",15,"bold"))
color_label.place(relx=0.5,rely=0.5,anchor=CENTER)

#Class
class randomizer():
    def __init__(self):
        self.__score = 0
    def updateColor(self):
        self.color = ["red","purple","maroon","skyblue","yellow","lightgreen","teal"]
        self.text_color = ["RED","PURPLE","MAROON","SKYBLUE","YELLOW","LIGHTGREEN","TEAL"]
        labelColor = random.choice(self.color)
        textColor = random.choice(self.text_color)
        color_label["fg"] = labelColor
        color_label["text"] = textColor
        color_label["font"] = labelColor
        
#Object
object1 = randomizer()

#Button
btn1 = Button(window,text="Change Color",bg="white",fg="black",font=("Inter",20,"bold"),command=object1.updateColor)
btn1.place(relx=0.5,rely=0.6,anchor=CENTER)

#Run Statement
window.mainloop()