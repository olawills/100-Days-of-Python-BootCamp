# Day 4 Python Bootcamp
import random


# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# Write a virtual coin toss program.. it will randomly tell the user "Heads" or "tails"

# print("Welcome to the dice Game!...")
# random_side = random.randint(0, 1)

# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")


# List

# fruits = ["Cherry", "Berry", "Pear", "Orange", "Mango"]

# fruits[3] = "Cheese"
# fruits.append("Williamsland")
# print(fruits)

# names_string = input("Give me everybody's names, seperated by a comma.\n ")
# names = names_string.split(", ")

# num_items = len(names)

# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + " is going to buy the meal today..")


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "x"

# print(f"{row1}\n{row2}\n{row3}")



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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_choice >= 3 or user_choice < 0:
    print("You inserted an invalid number, You lose try again..")
else:
    print(game_images[user_choice])
    
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[computer_choice])


    if computer_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("You Draw")


