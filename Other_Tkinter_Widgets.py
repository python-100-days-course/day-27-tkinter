# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 27 - Intermediate - Tkinter, *args, **kwargs and Creating GUI Programs
# Covers: label, button, entry, text (entry box), spinbox (counter), scale (slider), checkbutton, radiobutton, listbox
# Other_Tkinter_Widgets.py is created by Angela Yu

from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text", font=("Arial", 16, "bold"))
label.config(text="This is new text (label)")
label.pack()

#Buttons
def action():
    print("Do something")
label_2 = Label(text="\nButton:")
label_2.pack()
#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
label_3 = Label(text="\nEntry:")
label_3.pack()
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Textbox (multi line text)
label_4 = Label(text="\nTextbox:")
label_4.pack()
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
label_5 = Label(text="\nSpin:")
label_5.pack()
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
label_6 = Label(text="\nScale:")
label_6.pack()
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
label_7 = Label(text="\nCheckbutton:")
label_7.pack()
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
label_8 = Label(text="\nRadiobutton:")
label_8.pack()
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
label_9 = Label(text="\nListbox:")
label_9.pack()
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()