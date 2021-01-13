from imge_character import ChoseImgage
from Layout import showimgeCharter
class Character:
    def __init__(self, Name ,cognomen ,Maxhp ,MaxAtk ,Element ,Race ,Style ,Specialty ,Gender,Voice_Actor ,Weapon ):
        self.Name = Name
        self.cognomen = cognomen
        self.Maxhp = Maxhp
        self.MaxAtk = MaxAtk
        self.Element = Element
        self.Race = Race
        self.StyLe = Style
        self.Specialty = Specialty
        self.Gender = Gender
        self.Voice_Actor = Voice_Actor
        self.Weapon = Weapon
    
    def SetOGi(self,OgiName , Effect):
        self.Ogi = OgiName
        self.Effect = Effect
    
    def SetSkills1(self ,name ,Cooldown , Duration , Obtained , Effect):
        self.Skills1 = Skills1(name ,Cooldown , Duration , Obtained , Effect)
        

    def SetSkills2(self ,name ,Cooldown , Duration , Obtained , Effect):
        self.Skills2 = Skills2(name ,Cooldown , Duration , Obtained , Effect)
        
        
        

    def showOgi(self):

        return "โอกิ : {} \n Effect : {}".format(self.Ogi,self.Effect)
        

    def showSkills1(self):
        
        return  "สกิล 1 \n ชื่อท่า :{} \n Cooldown: {} \n Duration: {} \n Obtained: {} \n Effect: {}".format(self.Skills1.Name , self.Skills1.Cooldown , self.Skills1.Duration , self.Skills1.Obtained , self.Skills1.Effect)
        
    def showSkills2(self):

        return "สกิล 2 \n ชื่อท่า :{} \n Cooldown: {} \n Duration: {} \n Obtained: {} \n Effect: {}".format(self.Skills2.Name , self.Skills2.Cooldown , self.Skills2.Duration , self.Skills2.Obtained , self.Skills2.Effect)
        

    def showImage(self):

        try: 
            return showimgeCharter(self.Name)
        except IOError: 
            return print("read can not")

        

    def __str__(self):
        return "ชื่อตัวละคร : {} \n เพศ :{} \n ฉายา : {} \n พลังชีวิต : {} \n พลังโจมตี : {} \n ธาตุประจำตัว : {} \n เผ่า : {} \n เด่นด้าน : {} \n ความถนัด :{} \n นักพากย์ : {}  \n อาวุธประจำตัว : {} ".format(self.Name,self.Gender ,self.cognomen , self.Maxhp , self.MaxAtk , self.Element , self.Race , self.StyLe ,self.Specialty ,self.Voice_Actor, self.Weapon)



class Skills1:
    def __init__(self,Name ,Cooldown , Duration , Obtained , Effect):
        self.Name = Name
        self.Cooldown = Cooldown 
        self.Duration = Duration
        self.Obtained = Obtained
        self.Effect = Effect
    
class Skills2:
    def __init__(self,Name ,Cooldown , Duration , Obtained , Effect):
        self.Name = Name
        self.Cooldown = Cooldown 
        self.Duration = Duration
        self.Obtained = Obtained
        self.Effect = Effect

class Skills3:
    def __init__(self,Name ,Cooldown , Duration , Obtained , Effect):
        self.Name = Name
        self.Cooldown = Cooldown 
        self.Duration = Duration
        self.Obtained = Obtained
        self.Effect = Effect




def listToString(rh):
     str1 = " " 
     Specialty = str1.join(rh) 
     return Specialty  
    
        
 

