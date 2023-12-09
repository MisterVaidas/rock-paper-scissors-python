# Final day-4 project: Rock paper scissors

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


list_of_signs = [rock, paper, scissors]

user_choice = input("Please choose your option: enter 0 for rock, 1 for paper, and 2 for scissors ")

user_choice_to_int = int(user_choice)

if user_choice_to_int == 0:
  print(rock)
elif user_choice_to_int == 1:
  print(paper)
else:
  print(scissors)
  
computer_choice = random.randint(0, 2)
print(list_of_signs[computer_choice])

if user_choice_to_int == computer_choice:
  print("It's a draw!")
elif (user_choice_to_int == 0 and computer_choice == 1) or \
     (user_choice_to_int == 1 and computer_choice == 2) or \
     (user_choice_to_int == 2 and computer_choice == 0):
  print("You lose!")
else:
  print("You win!")