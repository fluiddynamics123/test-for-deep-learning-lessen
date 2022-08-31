import random
import math

def call_name_power(a):
  if a == 0:
    type = "fire"
    HP = 150
    speed = 120
  elif a == 1:
    type = "water"
    HP = 130
    speed = 130
  else:
    type = "leaf"
    HP = 180
    speed = 80
  return type,HP,speed

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

# 技の種類
moves = [
  {
    'name': 'light Attack',
    'power': 40,
    'accuracy': 100
  },
  {
    'name': 'Middle Attack',
    'power': 60,
    'accuracy': 80
  },
  {
    'name': 'Heavy Attack',
    'power': 80,
    'accuracy': 60
  }
]

# 技の選択
def select_move():
  while True:
    move_idx = int(input('select move: 0:light, 1:middle, 2:heavy'))
    if move_idx == 0 or move_idx == 1 or move_idx == 2:
      print('selected: ' + moves[move_idx]['name'])
      return moves[move_idx]
    else:
      print("Chose the number from 0 to 2!!")

# 命中判定(命中したかどうかのフラグを返す)
def calculate_accuracy(move):
  accuracy = move['accuracy']
  rand = random.randint(0, 100)
  if accuracy >= rand:
    print('Hit!!')
    return True
  else:
    print('Miss...')
    return False

# 命中判定(命中したかどうかのフラグを返す)
def calculate_accuracy(move):
  accuracy = move['accuracy']
  rand = random.randint(0, 100)
  if accuracy >= rand:
    print('Hit!!')
    return True
  else:
    print('Miss...')
    return False

# 攻撃によるHP計算
def calculate_hp(move, HP_defender, omega_attacker):
  power = move['power']
  HP_defender -= power*omega_attacker
  return HP_defender

# 攻撃(引数で攻撃者がplayerかどうか指定)
def attack(is_player_attack):
  if(is_player_attack):
    HP_defender = HP_opp
    omega_attacker = omega_self
    move = select_move()
  else:
    HP_defender = HP_self
    omega_attacker = omega_opp
    move = moves[random.randint(0, 2)]

  is_hit = calculate_accuracy(move)
  # 命中した場合攻撃を実行
  if is_hit:
    HP_defender = calculate_hp(move, HP_defender, omega_attacker)

  return HP_defender

def main():
  global type_self, HP_self, speed_self # プレイヤーのポケモンのステータス
  global type_opp ,HP_opp, speed_opp # 相手のポケモンのステータス
  global omega_self, omega_opp  # 相性による重み係数

  while True:
    which_pokemon = int(input("which pokemon do you use? (0:fire, 1:water, 2;leaf): "))
    if which_pokemon <= 2:
      print("\n")
      break
    else:
      print("Chose the number from 0 to 2!!")

  print("Your Pokemon")
  type_self, HP_self, speed_self = call_name_power(which_pokemon)
  print ("type is ..." + type_self)
  print ("HP is ..." + str(HP_self))
  print ("SPEED is ..." + str(speed_self))
  print("\n")

  opponent_pokemon = random.randint(0,2)
  type_opp ,HP_opp, speed_opp = call_name_power(opponent_pokemon)
  print("Opponent's Pokemon")
  print ("type is ..." + type_opp)
  print ("HP is ..." + str(HP_opp))
  print ("SPEED is ..." + str(speed_opp))
  print("\n")

  print("Level setting...")
  omega_self = omega_opp = 1.0
  if type_self != type_opp:
    omega_self,omega_opp = call_relation(type_self,type_opp) #相性による重み係数の呼び出し
  level_self = random.randint(1,50) #自分、相手のポケモンのレベルはランダムにしてます
  level_opp = random.randint(1,50)

  HP_self = int(math.sqrt(level_self)*HP_self) #HPは平方根を乗する
  speed_self = int(math.log(math.e + level_self -1)*speed_self) #speedはln(e + level -1)を乗する
  HP_opp = int(math.sqrt(level_opp)*HP_opp)
  speed_opp = int(math.log(math.e + level_opp -1)*speed_opp)

  print("Your pokemon's type / level / HP / speed...")
  print("      " + type_self + " / " + str(level_self) + " / " + str(HP_self) + " / " + str(speed_self) )
  print("opponent pokemon's type / level / HP / speed...")
  print("      " + type_opp + " / " + str(level_opp) + " / " + str(HP_opp) + " / " + str(speed_opp) )
  print("\n")

  print("Battle start\n")
  while HP_self > 0 and HP_opp > 0:
    if speed_self >= speed_opp:
      print("Your Attack")
      HP_opp = attack(is_player_attack = True)
      print("opponent HP is..." + str(HP_opp) + '\n')

      print("Opponent's Attack")
      HP_self = attack(is_player_attack = False)
      print("your HP is..." + str(HP_self) + '\n')

    elif speed_self < speed_opp:
      print("Opponent's Attack")
      HP_self = attack(is_player_attack = False)
      print("your HP is..." + str(HP_self) + '\n')

      print("Your Attack")
      HP_opp = attack(is_player_attack = True)
      print("opponent HP is..." + str(HP_opp) + '\n')
    else:
      pass

  # 戦闘終了時のメッセージ
  if(HP_self > 0):
    print('You win!!')
  elif(HP_opp > 0):
    print('You lose...')

if __name__ == "__main__":
    main()