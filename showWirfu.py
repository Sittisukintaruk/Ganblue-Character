import FireCharacter 
import os
from Character import Characterdictionary,Characterlist,Characterclass

def showCharater():
    FireCharacter.setIndex()
    print(Characterlist[0].showImage())
    # for count in range (len(Characterlist)):
    #     print(Characterlist[count])
    #     print(Characterlist[count].showOgi())
    #     print(Characterlist[count].showSkills1())
    #     print(Characterlist[count].showSkills2())
    #     print(Characterlist[count].showImage())

  
    
    


if __name__ == "__main__" :
    showCharater()
    

