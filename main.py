#users wizards,

class User(): #equivalent to class User(object)
  
  def __init__(self,email):
    self.email=email

  def sign_in(self):
    print('logged in')

  # def attack(self):
  #   print('do nothing')


class Wizard(User):
  def __init__(self,name,power,email):
    self.name= name
    self.power = power
   # User.__init__(self,email) 
   #alternatively use super
    super().__init__(email) # no need to pass self


  def attack(self):
     # User.attack(self);
      print(f'attacking with power of {self.power}')
  


class Archer(User):
  def __init__(self,name,num_arrows):
    self.name= name
    self.arrows = num_arrows

  def attack(self):
      print(f'attacking with arrows: arrows left {self.arrows}')

#intrsopection
wizard1 = Wizard('Merlin',50,'merlin@cat.com')
archer1 = Archer('Robin',100)

#dir - abilty to detemine the type of object , examine the object what methods ,attributes that the instance has with dir method 
print(dir(wizard1))
print(wizard1.email)

print(wizard1.attack())
print(archer1.attack())

def player_attack(char):
  char.attack()


player_attack(wizard1)
player_attack(archer1)


for char in [wizard1,archer1]:
  char.attack()



#using isistance Note : subclass is an instance of parent class
#object is the base that python comes with. This object class provides all the dunder methods 
print(isinstance(wizard1,User))
print(isinstance(wizard1, object))