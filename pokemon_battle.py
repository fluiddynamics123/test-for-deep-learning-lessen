import random

def call_name_power(a):
  print(a)
  if a == 0:
    type = "fire"
    HP = 150
    SPEAD = 120
  elif a == 1:
    type = "water"
    HP = 130
    SPEAD = 130
  else:
    type = "leaf"
    HP = 180
    SPEAD = 80
  return type,HP,SPEAD

def call_relation(self,opp):
  if self == "leaf":
    if opp == "fire":
      omega_s = 0.8
      omega_opp = 1.2
    elif opp == "water":
      omega_s = 1.2
      omega_opp = 0.8
    else:
      pass
  elif self == "water":
    if opp == "fire":
      omega_s = 0.8
      omega_opp = 1.2
    elif opp == "leaf":
      omega_s = 1.2
      omega_opp = 0.8
    else:
      pass
  else:
    if opp == "water":
      omega_s = 1.2
      omega_opp = 0.8
    elif opp == "leaf":
      omega_s = 0.8
      omega_opp = 1.2 
    else:
      pass
  return omega_s,omega_opp   

while True:
  which_pokemon = int(input("which pokemon do you use? 0:fire, 1:water, 2;leaf"))
  if which_pokemon <= 2:
    break
  else:
    print("Chose the number from 0 to 2!!")
    
print("you chose" + str(which_pokemon))
type_self,HP_self,spead_self = call_name_power(which_pokemon)
print ("type is ..." + type_self)
print ("HP is ..." + str(HP_self))
print ("SPEED is ..." + str(spead_self))

opponent_pokemon = random.randint(0,2)
type_opp,HP_opp,spead_opp = call_name_power(opponent_pokemon)
print ("type is ..." + type_opp)
print ("HP is ..." + str(HP_opp))
print ("SPEED is ..." + str(spead_opp))

print("Battle start")
omega_self = 1.0
omega_opp = 1.0
if type_self != type_opp:
  omega_self,omega_opp = call_relation(type_self,type_opp) #相性による重み係数の呼び出し
level_self = random.randint(1,50) #自分、相手のポケモンのレベルはランダムにしてます
level_opp = random.randint(1,50)
import math

HP_self = int(math.sqrt(level_self)*HP_self) #HPは平方根を乗する
spead_self = int(math.log(math.e + level_self -1)*spead_self) #speedはln(e + level -1)を乗する
HP_opp = int(math.sqrt(level_opp)*HP_opp)
spead_opp = int(math.log(math.e + level_opp -1)*spead_opp)

print("Your pokemon's type / level / HP / speed...")
print("      " + type_self + " / " + str(level_self) + " / " + str(HP_self) + " / " + str(spead_self) )
print("opponent pokemon's type / level / HP / speed...")
print("      " + type_opp + " / " + str(level_opp) + " / " + str(HP_opp) + " / " + str(spead_opp) )
while HP_self > 0 and HP_opp > 0:
  if spead_self >= spead_opp:
    print("Your Attack")
    HP_opp -= 25.0*omega_self
    print("opponent HP is..." + str(HP_opp))
    HP_self -= 25.0*omega_opp
    print("your HP is..." + str(HP_self))
  elif spead_self < spead_opp:
    print("Opponent's Attack")
    HP_self -= 25.0*omega_opp
    print("your HP is..." + str(HP_self))
    HP_opp -= 25.0*omega_self
    print("opponent HP is..." + str(HP_opp))
  else:
    pass