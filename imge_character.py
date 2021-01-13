# importing required packages 
from tkinter import *
from PIL import ImageTk, Image 

# creating main window 
# Image\Fire\Female\Stum_01.png

# arranging application parameters 
def ChoseImgage(Im):
    root = Tk() 
    img = ImageTk.PhotoImage(Image.open(Im))
    imge = Image.open(Im)
    # width , height = imge.size
    canvas = Canvas(root, width = 1080, height = 800) 
    canvas.pack() 

    # loading the image 
    img = ImageTk.PhotoImage(Image.open(Im)) 

    # arranging image parameters 
    # in the application 
    canvas.create_image(135, 20,image = img , anchor= NW) 

    # running the application 
    root.mainloop() 
