from tkinter import *
from Character import Characterdictionary

def Showdown(character):
    root = Tk()
    root.option_add("*font" , "consolas 25")
    char_Stats_dir = Characterdictionary.get("FireCharacter").get(character).get('Stats')
    characterlist = []
    characterlist_key = []

    f1 = Frame(root , bg = "blue")
    f1.pack(anchor = W)
    count = 0
    for k,v in char_Stats_dir.items():
        # print(k , " " , v)
        Lt = Label(f1 , text = k ,width = 15 )
        Lt.grid(row = count , column = 0)
        ls = Label(f1 , text = v  ,width = 15)
        ls.grid(row = count  , column = 1)
        count +=1 


        characterlist.append(v)
        characterlist_key.append(k)

    # print(characterlist)
    # print(characterlist_key)



    root.mainloop()



