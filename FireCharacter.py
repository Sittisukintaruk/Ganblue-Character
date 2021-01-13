from CharacterClass import Character , listToString
from Character import Characterdictionary,Characterclass,Characterlist



def setIndex():
    Characterclass.append("Sturm")
    Characterclass.append("Zeta")
    # print(Characterclass[0])
    for item in range(len(Characterclass)):
        Characterlist.append(SetCharacter(Characterclass[item]))


def set_chracter(name):
    Character_stats = Characterdictionary.get('FireCharacter').get(name).setdefault('Stats')
    statslists = [v for k,v in Character_stats.items()]
    Character_grablue = Character(statslists[0],statslists[1], statslists[2] ,statslists[3] ,statslists[4], statslists[5] , statslists[6] ,statslists[7] ,statslists[8] ,statslists[9],statslists[10])
    Character_grablue.Specialty = listToString(Character_grablue.Specialty)

    return Character_grablue

def set_ogi(name,Character_grablue):
    Character_ogi = Characterdictionary.get('FireCharacter').get(name).setdefault("Ogi")
    ogilists = [v for k,v in Character_ogi.items()]
    Character_grablue.SetOGi(ogilists[0] ,ogilists[1])

def set_skile(name,Character_grablue):
    Skile1 = Characterdictionary.get('FireCharacter').get(name).get('Skile').get("Skile1")
    Skile1lists = [v for k,v in Skile1.items()]
    Character_grablue.SetSkills1(Skile1lists[0],Skile1lists[1],Skile1lists[2], Skile1lists[3] , Skile1lists[4])
    
    Skile2 = Characterdictionary.get('FireCharacter').get(name).get('Skile').get('Skile2')
    Skile2lists = [v for k,v in Skile2.items()]
    Character_grablue.SetSkills2(Skile2lists[0],Skile2lists[1] ,Skile2lists[2], Skile2lists[3] ,Skile2lists[4])


def SetCharacter(name):
    #stats character
    Character_grablue = set_chracter(name)
    #Ogi stum
    set_ogi(name , Character_grablue)
    #Skile Stum
    set_skile(name,Character_grablue)

    #setCharacter
    return Character_grablue
     
    
# ตัวแรกธาตุไฟ Character_grablue
if __name__ == "__main__":
    setIndex()
    # for i in Characterlist:
    #     print(i.showOgi())
   

    

    




