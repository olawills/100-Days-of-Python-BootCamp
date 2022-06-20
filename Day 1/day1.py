# Day 1 of Python Bootcamp
print("Day 1: Python Print Function\nThe Function is decleared like this:")
print("print('what to print')")

# String and String Manipulation
print("Hello" + " " + "Olabamidele") # String Concatenation
name = input("What is your name: ")
print("Hello " + name)

print("Hello" + " " + input("What is your name: "))

#Use of Input Functions!
nameOfCharacters = input("Enter your name: ")
print(len(nameOfCharacters))

a = input("a: ")

b = input("b: ")

c = a
d = b
a = d
b = c
print("a = " + a)
print("b = " + b)

# Building a Band Name Generator
print("Welcome to the Band Name Generator..")
nameOfCity = input("What's name of the city you grew up in?\n")
nameOfPet = input("What's your pet name\n")
print("Your Band name could be " + nameOfCity + " " + nameOfPet)
