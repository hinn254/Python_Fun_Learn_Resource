# BANK
# check balance
# withdraw
# deposit

# input
# print
# operations
# variables - data

# Control Flow
# conditions
# if
# if else
# elif
# while
# pass
# continue

# if - condition - happen
# val = input("Do you want to proceed? enter Y for yes and N for no\t")

# if val == "Y":
#     print("HURRAY")
# elif val == "N":
#     print('Goodbye')
# else:
#     print("Invalid input, try again")


#  Simple bank acc
balance = 100
print("Welcome to Absa")
pin = 4321
# '4321' != 4321
pin_input = int(input("PLease enter your pin to proceed"))
if pin_input != pin:
    print("Thou areth a thiefeth")
else:
    fName = "Kone Basir"
    print("*"*30)
    print("Welcome " + fName)
    print("Your current balance is KES", balance)
    print("*"*30)
    user_action = input(
        "To withdraw enter w\n To deposit enter d\n To check balance enter b\n To quit enter q\n:")
    print(user_action)
    if user_action == "w":
        amt_withdrawn = int(input("Enter amnt to withdraw"))
        print(f"{amt_withdrawn} withdrawn! \nBalance is {balance - amt_withdrawn}")
        if amt_withdrawn > balance:
            print("You're broke")
    if user_action == 'b':
        print(f"Your balance is {balance}")
    if user_action == 'q':
        print(f"Goodbye")
    if user_action == 'd':
        dep = int(input("Enter amnt to be deposited >"))
        print(f"Your new balance is {dep + balance}")
