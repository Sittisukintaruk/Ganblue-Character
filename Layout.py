from tkinter import  *
from Layout_Stats import Showdown
from PIL import ImageTk, Image 
import os

def showimgeCharter(chacrter):
    global on_offs ,count
    count = 0
  

    def on_lick (e):
        # print (e.widget.cget("text"))
        canvas.delete("all")
        photo = e.widget.cget("text")
        index = Art.index(photo)
        canvas.create_image(100, 0,image = img_list[index] , anchor= NW) 
    def on_off_clik(e):
        if chk1.get():
                
            print("is : ",chk1.get())
        else:
            Showdown(chacrter)
            print(" : ",chk1.get())
            
    
    root = Tk()
    # root.geometry("805x784")
    root.resizable(0,0)
    root.title("Test")
    root.option_add("*font" , "consolas 20")    
    Art = ['Base Art' , '2nd Art' , 'Story Art']

    f1 = Frame(root , bg = 'red')
    f1.grid(row = 0 , columnspan = 2 ,sticky="NESW")

    f2 = Frame(root, bg = "blue")
    f2.grid(row  = 1 , columnspan = 2, sticky = "NESW")

    img_list = []

    canvas = Canvas(f2, width = 1080, height =800) 
    canvas.pack(padx = 5 ,pady = 5 ,fill = X ) 
    # loading the image 
    imgse = Image.open(f"Image/Fire/Female/{chacrter}/Base Art.png")
    img_lists = ImageTk.PhotoImage(imgse)
    canvas.create_image(100, 0,image = img_lists , anchor= NW) 

    tv_code = StringVar()
    tv_code.set('Base Art') 
    
    on_off = StringVar()
    on_off.set("off")
    on_offs = False
    chk1 = BooleanVar()

    for i,name in enumerate(Art):   
        imgs = Image.open(f"Image/Fire/Female/{chacrter}/{name}.png")
        img_list.append(ImageTk.PhotoImage(imgs))
        btn = Radiobutton(f1,text = name ,value = name ,variable = tv_code  ,width = 15 ,indicatoron = False , bg = "gold")
        btn.pack(side = LEFT , padx = 20 , pady = 20 ,ipadx = 5 , ipady = 10 ,anchor = W)
        btn.bind("<Button-1>" , on_lick)
        

    bt = Checkbutton(f1 , text = "Stats"  ,variable = chk1  , width = 15 ,indicatoron = False )
    bt.pack(side = LEFT ,padx = 20 , pady = 20 ,ipadx = 5 , ipady = 10 ,anchor = W)
    bt.bind('<Button-1>' , on_off_clik)
    root.mainloop()





