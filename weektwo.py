# break
# continue
# while 
# == = !=  
# a = 100
# b = 2
# import time

# 100 < 100
# 100 <= 100

# while b <= a:
#     print("kai")
#     print("Inside while")
#     print("Before break")
#     print(b)
#     b =b + 1

#     if b == a:
#         print("EQUAL")
#         continue
#         print("After break")
#     # time.sleep(1)
# else:
#     print("a is more than 100")
# print("oUTSIDE WHILE")

# q = "Kai" - assignment
# q = "benm"
# q - variable - retrieve assign/hold
#  == - compare / False / True 
#   != - NOT EQUAL\



# age = input
# c = 2
# d = 5

# print(c==d)

# BOOLEANS
# True or False
# 2==2 - True
# 3 == 2 - False

# if 2==2:
#     print('sadsadasd')
# name = input("Your name ?\nname\r")


import time,getpass
pin = ""
total_attempts = 3
amount = 0
current_attempt = 0

print("Welcome to our bank")
pin = getpass.getpass("Enter your new pin")

print("*"*30)
print("-"*30)
print("\t\tKCB BANK")
print("-"*30)
print("*"*30)
time.sleep(4)
while current_attempt < total_attempts:
    user_pin = int(input("Enter your pin: \t"))
    if user_pin == int(pin):
        #  BANK LOGIC = D,W,B
        print("Verified")
        # CODE FOR D,W,CHECK BALANCE
    else:
        print("Wrong pin")
        current_attempt = current_attempt + 1
        remaining = total_attempts - current_attempt
        print(f'Your remaining with {remaining} attempts')
        if current_attempt == total_attempts:
            print("Blocked")



























