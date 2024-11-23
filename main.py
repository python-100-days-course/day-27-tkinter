# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 27 - Intermediate - Tkinter, *args, **kwargs and Creating GUI Programs
# Covers: label, button, entry, more in Other_Tkinter_Widgets.py
# Tkinter Layout Managers: pack(), place(), grid()
# Padding

from tkinter import *
# This way "tkinter.____" doesn't need to be used, however using "import tkinter" is more clear, in this case it's fine, since only tkinter is imported as "*"

# Create a window
window = Tk()
window.title("My 1st GUI App") # window title
window.minsize(width=500, height=300) # minium size of the window
window.config(padx=20, pady=20) # adds space around all four edges

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold")) # create label component
# my_label.pack() # place a component on screen and automatically center, options - side, expand, etc.
my_label.grid(column=0, row=0) # used to place the component into the window

# Buttons, entry, and setting component options

# Update properties/configs of a created components:
my_label["text"] = "New Text"
my_label.config(text="Another New Text", padx=30, pady=30) # padding can also be added around components

# Button
def button_clicked():
    # Challenge 1: show "button  got clicked" on my_label when the button gets clicked
    my_label.config(text="Button Was Clicked!")
    # Challenge 2: make the typed text in the entry components display as text in my_label (top of the screen)
    new_text = input.get()
    my_label.config(text=new_text) # .get() # returns input of the entry components
button = Button(text="Click Me", command=button_clicked)
# button.pack() # used to add the button to screen
button.grid(column=1, row=1)

# Another Button
button_2 = Button(text="Click Me 2")
# button.pack() # used to add the button to screen
button_2.grid(column=2, row=0)

# Entry component - input
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

# Advanced Python Arguments
# Arguments with Default Values (no inputs required):
    # def my_function(a=1, b=2, c=3):
        # Do this with a
        # Then do this with b
        # Finally do this with c

# *args: Many Positional Arguments
    # def add(*args):
        # for n in args:
            # print(n)
    # See more examples in playground .py

# **kwargs: Many Keyword Arguments (see example in playground .py)
    # With .get() keyword arguments are optional when the object is initiated

# Fun Fact: Tkinter is ported from Tk written by John Ousterhout while at Berkley, this why Tkinter ended up using **kw

# Buttons, entry, and setting component options

# pack() - packs widgets next to each other in a logical format, by default starts at the top
    # can be packed starting left, right or bottom
    # difficult for price positioning

# place() - precise positioning with x and y values
    # example: my_label.place(x=0, y=0)
    # downside is that it's too specific

# grid() - imagines that entire window is a grid then components can be placed inside this grid via column and row
    # good balance between precision and flexibility

# Note: pack(), place() and grid() can't be mixed, only one should be used



# Keeps the window on screen and listens for what the user will do to interact with it, stays at the end
window.mainloop()