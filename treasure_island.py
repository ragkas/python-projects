print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure by making wise choices!")
name = input("What is your name?\n")
crossroad = input(f"Hello {name}, You find yourself at a crossroad. Which path will you choose? Left or Right.\n")
if crossroad.lower() == "left":
    print("You chose the left path. A dense forest lies ahead.")
    forest = input("Continue through the forest or Climb a tree to get a better view. Continue or Climb.\n")
    if forest.lower() == "climb":
        print("You climb a tree to get a better view...From above, you spot a mysterious house.")
        print("You arrive at the entrance of the house.")
        cave = input("In the dim light, you see three doors. Which one do you want to enter Blue, Green or Orange?\n")
        if cave.lower() == "orange":
            print("As you open the orange door, you see a glimmer of light.")
            print(f"Congratulations {name}! You've found the hidden treasure!")
        elif cave.lower() == "blue":
            print("You enter a room full of scorpions. Game over.")
        elif cave.lower() == "green":
            print("You enter a room of zombies. Game over.")
        else:
            print("Your choice does not exist. Game over.")
    elif forest.lower() == "continue":
        print("You continue through the dense forest.")
        print("You encounter a a tiger and it killed you. Game over.")
    else:
        print("Your choice does not exist. Game over.")
elif crossroad.lower() == "right":
    print("You chose the right path. A wild river blocks your way.")
    print("You attempt to swim across the river...")
    print("Oops! The current is too strong, and you're swept away. Game over!")
else:
    print("Your choice does not exist. Game over.")