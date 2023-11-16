import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
outcomes = [rock, paper, scissors]
userChoice = int(input("What do you choose? Type 0 for Rock 1 for Paper or 2 for Scissors.\n"))
if userChoice < 0 or userChoice >= 3:
    print("Invalid choice.")
else:
    print("You chose:\n")
    print(outcomes[userChoice])

    computerChoice = random.randint(0,2)

    print(f"Computer chose:")
    print(outcomes[computerChoice])

    if userChoice == 0 and computerChoice == 2:
        print("You win!")
    elif userChoice == 2 and computerChoice == 0:
        print("You lose.")
    elif userChoice < computerChoice:
        print("You lose.")
    elif userChoice > computerChoice:
        print("You win!")
    elif userChoice == computerChoice:
        print("It's a tie")
