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

#HOUSE shape (square) CODE
square = drawpad.create_rectangle(600,200,200,550, fill='red')
# ROOF CODE
line = drawpad.create_line(400,0,600,200)
line = drawpad.create_line(200,200,400,0)

# 80pt: Square windows and a door
#WINDOWS CODE
squarewindow = drawpad.create_rectangle(320,250,250,330, fill='white')
squarewindow = drawpad.create_rectangle(480,250,550,330, fill='white')
#DOOR CODE
door = drawpad.create_rectangle(350,550,450,350, fill='dark gray')

# 90pt: A door handle plus a chimney!
#DOOR HANDLE CODE
doorhandle = drawpad.create_oval(360,450,370,460, fill='black')
#CHIMNEY CODE
chimney1 = drawpad.create_line(200,50,200,200)
chimney2 = drawpad.create_line(200,50,270,50)
chimney3 = drawpad.create_line(270,50,270,130)

# 100pt: Green grass on the ground and a red house!
#GREEN GRASS CODE
grass = drawpad.create_rectangle(0,550,900,800, fill='light green')
# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github
root.mainloop()