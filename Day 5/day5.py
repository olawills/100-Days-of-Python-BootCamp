# For Loops
from audioop import avg
from functools import total_ordering
import random

# fruits = ["Apple", "Cherry", "Orange"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# write a program that calculates the average student height from a List of heights

# student_heights = input("Input a list of student heights \n").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # print(student_heights)

# # total_height = sum(student_heights)
# # number_Of_students = len(student_heights)
# # 
# total_height = 0
# for height in student_heights:
#     total_height += height
# # print(total_height)

# number_of_student = 0
# for student in student_heights:
#     number_of_student += 1
# # print(number_of_student)

# average_height = round(total_height / number_of_student)
# print(average_height)

#  Write a program that calculates the highest score from a list of scores
# student_scores = input("Input a list of student scores \n").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_number = 0
# for number in student_scores:
#     if number > highest_number:
#         highest_number = number
# print(f"The higest score in the class is: {highest_number}")

# Range
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# Write a program that calculates the sum of all the even numbers from 1 to 100

# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(f"The sum of even numbers is: {total}")

# Write a program that automatically prints the solution to the FizzBuzz

# total = 0
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         total = number
#         print("FizzBuzz")
#     if number % 3 == 0:
#             total = number
#             print("Fizz")
#     elif number % 5 == 0:
#             total = number
#             print("Buzz")
   
#     else:
#         total = number
#         print(total)
    
    
# Password Generator..

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '<', '>', '?' ]
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password_letters = ""
# password_symbols = ""
# password_numbers = ""
# password_total = ""
# total_numbers = 0
# for char in range(0, nr_letters):
#         random_number = random.randint(0, 52)
#         password_letters += letters[random_number]
# total_numbers += nr_letters
        
# for char in range(0, nr_symbols):
#         random_number = random.randint(0, 11)
#         password_symbols += symbols[random_number]
# total_numbers += nr_symbols

# for i in range(0, nr_numbers):
#         random_number = random.randint(0, 9)
#         password_numbers += numbers[random_number]        
# total_numbers += nr_numbers
        
# password_total = password_letters + password_symbols + password_numbers
# password_total_2 = list[password_total]
# random.shuffle(password_total_2)
# password_total_3 = ''.join(password_total_2)
# print(f"Your password is {password_total_3}")

password_list = []

for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
        password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
        password_list.append(random.choice(symbols))
        

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
        password += char

print(f"Your password is {password}")
