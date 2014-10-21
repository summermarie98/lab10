##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# 70pt: House outline (roof and the house)

#HOUSE shape (square)
square = drawpad.create_rectangle(600,200,200,550, fill='red')
# ROOF
line = drawpad.create_line(400,0,600,200)
line = drawpad.create_line(200,200,400,0)

# 80pt: Square windows and a door
#WINDOWS
squarewindow = drawpad.create_rectangle(320,250,250,330)
squarewindow = drawpad.create_rectangle(480,250,550,330)
#DOOR
door = drawpad.create_rectangle(350,550,450,350)

# 90pt: A door handle plus a chimney!
#DOOR HANDLE
doorhandle = drawpad.create_oval(360,450,370,460)
#CHIMNEY

# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github
root.mainloop()