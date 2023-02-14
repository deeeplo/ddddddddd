
class User():
    def __init__(self,fName,lName,permission=1,login_attemps=0):
        self.fName = fName
        self.lName = lName
        self.permission = permission
        self.loginattempts = login_attemps
        self.Privilege = Privilege(self.permission) 
    
    def describe_user(self):
        print(f"The user is {self.lName}, {self.fName} and has a permission level of {self.permission}")
    
    def greet_user(self):
        print(f"Hello {self.fName} {self.lName}!")

    def increment_login_attempts(self):
        self.loginattempts +=1
    
    def reset_login_attempts(self):
        self.loginattempts = 0

class Admin(User):
    def __init__(self,fName,lName,permission=5):
        super().__init__(fName,lName,permission)

class Privilege():
    def __init__(self,permission):
        self.permission = permission
        
    def show_privileges(self):
        privlist = ["post ","delete posts ","ban users ","delete all posts ","access backend "]
        print("User can ",end='')#add coomnas later
        if self.permission > len(privlist):
            for i in range (len(privlist)):
                print(privlist[i],end='')
            
        else:
            for i in range (self.permission):
                print(privlist[i],end='')
       



        
