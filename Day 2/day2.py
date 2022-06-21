# Day 2...
# print(len("Williams"))

# print("Williams"[7])

# james = str(input("Enter any number: "))
# print("Hello " + james)

# Data Types
# String
#float
# Boolean
#Integer

# numOfChars = str(len(input("What is your name: ")))
# print("Your name has " + numOfChars + " Characters...")

# print(70 + float("100.5"))

# a = float(235)
# print(type(a))

# Data Types Exercises...


# two_digit_number = input("Enter a three digits number: ")
# first = int(two_digit_number[0])
# second = int(two_digit_number[1])
# third = int(two_digit_number[2])
# print(first + second + third)

# BMI CALCULATOR...

# height = int(input("Enter your height in m: "))
# weight = int(input("Enter your weight in kg: "))
# height = height ** 2

# #print(round(weight / height, 2))
# bmi_calculator = round(weight / height, )
# print(f"Your BMI is {bmi_calculator} Percentile")

# Number Manipulation...

#  Program to get your age left if your to live for 90 years
# age = int(input("What is your current age? "))

# years_remaining = 90 - age
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# message = f"You have {years_remaining} years, {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left"
# print(message)

#Building A Tip Calculator

print("Welcome to the tip calculator!..")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")


