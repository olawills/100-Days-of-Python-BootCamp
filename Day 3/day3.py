# Day 3...
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age "))
    if age < 12:
        bill = 5
        print("Child ticket are to pay $5")
    elif age <= 18:
        bill = 7
        print("Teenagers ticket are to pay $7")
    elif age <= 21:
        bill = 9
        print("Youth ticket are to pay a $9 ticket as you are an adult")
    elif age <= 25:
        bill = 10
        print("Young Adult ticket are to pay a $10 ticket")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You get a free ticket ")
    else:
        bill = 12
        print("Please pay $12")
        
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your final bill is ${bill}")
        
else:
    print("You are not up to the height!....")
    
    
number = int(input("Which number do you want to check "))

if number % 2 == 0:
    print("This is a even number")
         
else:
    print("This is an odd number")    

# Write a program that interpretes the Body Mass Index (BMI based on a user's weight and height

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
height = height **2

BMI = weight / height
BMI_TOTAL = round(BMI, 1)

if BMI < 18.5:
    print(f"Your BMI is {BMI_TOTAL}, You are underweight.. ")
elif BMI < 25:
    print(f"Your BMI is {BMI_TOTAL}, You have a normal wieght.. ")
elif BMI < 30:
    print(f"Your BMI is {BMI_TOTAL}, You are overweight.. ")
elif BMI < 35:
    print(f"Your BMI is {BMI_TOTAL}, You are obese.. ")
else:
    print(f"Your BMI is {BMI_TOTAL}, You are clinically obese.. ")
    
# Write a program that works out whether if a given year is a leap year.. 

leap_input = int(input("Enter a year "))

if leap_input % 4 == 0:
    if leap_input % 100 == 0:
        if leap_input % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap year")
else:
    print("Not a Leap Year")


# Build an automatic pizza order program, Based on a user's order, work out their final bill..

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
    
elif size == "M":
    bill += 20
    
else:
    bill += 25
    
    
if add_pepperoni == "Y":
    if size == "S":
        bill  += 2
    else:
        bill += 3
        
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is ${bill}")

# Love Calculator..
# Write a program that tests the compatibility between two people.

print("Welcome to the Love Calculator!.. ")
name1 = input("What is your name? \n")
name2 = input("What is the name of your Crush? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v= lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
print(f"Your score is {love_score}")
# love_total = str(love_score)

if (love_score < "10") or (love_score > "90"):
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif (love_score >= "40") and (love_score <= "50"):
    print(f"Your score is {love_score}, you are alright together")
    
else:
    print(f"You score is {love_score}")

# Project Treasure Island...

print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[Olawills]
*******************************************************************************''')

print(''' Welcome To Treasure Island
       _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')

print("Your mission is to find the missing Treasure")
question1 = input("You\'re at a cross road. Where do you want to go? Type \"left\" or \"right\" ")


combined_question1 = question1.lower()


if combined_question1 == "right" or combined_question1 == "":
    print("fall into a hole Game Over!..")
elif combined_question1 == "left":
    question2 = input("You\'ve come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    conbined_question2 = question2.lower()
    if conbined_question2 == "swim" or conbined_question2 == "":
        print("Got attacked by a trout Game Over!..")
    elif conbined_question2 == "wait":
        question3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
        combined_question3 = question3.lower()
        if combined_question3 == "blue":
            print("Eaten by beast Game Over!..")
        elif combined_question3 == "red":
            print("Burned by fire!.. Game Over!..")
        elif combined_question3 == " ":
            print("Game Over Please choose out of the three doors")
        else:
            print("You win")
