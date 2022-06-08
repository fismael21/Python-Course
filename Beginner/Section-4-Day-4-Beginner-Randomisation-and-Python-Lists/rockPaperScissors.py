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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

list_of_choices =[rock, paper, scissors]
computer_choice = random.randint(0, 2)
choice_computer = list_of_choices[computer_choice]


if (choice == 0): # If you choose rock
  print(rock)
  print(f"The computer chose {computer_choice}")
  print(choice_computer)
  if(computer_choice == 0):
    print("It is a draw!")
  elif (computer_choice == 1):
    print("You lost!")
  else:
    print("You won!")
elif (choice == 1): # If you choose paper
  print(paper)
  print(f"The computer chose {computer_choice}")
  print(choice_computer)
  if(computer_choice == 0):
    print("You won!")
  elif (computer_choice == 1):
    print("It is a draw!")
  else:
    print("You lost!")
elif (choice == 2): # If you choose scissors
  print(scissors)
  print(f"The computer chose {computer_choice}")
  print(choice_computer)
  if(computer_choice == 0):
    print("You lost!")
  elif (computer_choice == 1):
    print("You win!")
  else:
    print("It is a draw!")
else:
  print("You must write a number beetween 0 and 2!")