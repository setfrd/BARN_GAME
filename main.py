
from secrets import choice


print('''

                             +&-
                           _.-^-._    .--.
                        .-'   _   '-. |__|
                       /     |_|     \|  |
                      /               \  |
                     /|     _____     |\ |
                      |    |==|==|    |  |
  |---|---|---|---|---|    |--|--|    |  |
  |---|---|---|---|---|    |==|==|    |  |
''')
print("Welcome to the GET TO BARN")
print("The metior just hit the farm and there is ZOMBIE invasion happening you need to get to safety as soon as possible!!!")
print("Youur mission is to get to the barn safely!")

choice1 = input('You\'re at the house you need to cross the cow farm because it is toxic. Whitch side you want to go? Type "left" or "right".\n').lower()


if choice1 == "right":
  choice2 = input('You\'ve come to the corn field. You can rest to get some energy or continue to the cotton field. Type "wait" to wait to get energy. Type "run" to run across.\n').lower()
  if choice2 == "wait":
      choice3 =input("You arrive at the barn unharmed. There is 3 doord to the barn. One red, one yellow and one blue. Which colour do you choose? \n").lower()
      if choice3 == "red":
          print("It's a room full of fire. Game Over.")
      elif choice3 == "yellow":
          print("It's a room full of mutant horses and they attacked you. Game Over.")
      elif choice == "blue":
          print("You got inside the barn safely. You Won!")
      else:
          print("You choose the door that doesn't exist. Zombies got you!")
  else:
      print("You were attacked by giant spiders and eaten to death. Game Over.")
else:
  print("You fell into a hole. Game Over!")