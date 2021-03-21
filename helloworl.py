# python --version
# import requests


####################################################
#   TODAY'S LESSONS
####################################################
# PRINT
# print('Hello, World!')
# print(1 + 2)
# print(7 * 6)
# print('Name', 'hiin')
# print("The end", "or is it?", "keep watching to learn more about Python", 3)
# Strings
# Variables
# Operations
# Integers
# Array methods


# print("Hello \rworld")
# ESCAPE CHARACTERS
# input("First Name \r")

# Strings

# name = "ben"
# greeting = "hello"
# number = 341242343
# print(greeting + " " + name + str(34234324))
# #  f -string

# print(f"{greeting} {name} {number}")
# f" {name} "

# message = "Welcome to our Mall...Happy Shopping!"

# STEPS
# print("Welcome to JUJA CITY MALL")
# fName = input("Enter first Name: ")
# print(fName + " " + message)

p_bananas = 20
p_shoes = 2300
print('*' * 70)
print("\t\t\tWelcome to Juja mall")
print('*' * 70)

full_name = input("Enter full name\t")
number_of_bananas = int(input("How many bananas did you buy\n"))
number_of_shoes = int(input("How many shoes did you buy\n"))
print('-' * 10)

amnt_bananas = number_of_bananas * p_bananas
amnt_shoes = number_of_shoes * p_shoes

print(f"{full_name} you have spent KES{amnt_bananas} on bananas and KES{amnt_shoes} on shoes \nYour total spending KES{amnt_shoes + amnt_bananas}")
print('*' * 30)
