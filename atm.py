import sys

import numpy as np

# <firstname> <lastname> <bsb> <account no> <balance>

# check if enough arguments
if len(sys.argv) != 6:
    print("ERROR: Not enough arguments supplied")
    sys.exit()

# store data in a list
atm_data = sys.argv[1::]

# assign balance to float variable, last argument balance
balance = float(atm_data[4])

# notes in a list
notes = [50, 20, 10, 5]


# atm continue function
def atm_continue():
    if input("Do you want to continue? Y/N ") == "N":
        print("Have a nice day!")
        sys.exit()

while True:

    user_input = input()

    if user_input == "quit":
        print("Have a nice day!")
        sys.exit()

    if user_input == "balance":
        print(atm_data[0], atm_data[1])
        print("BSB: " + atm_data[2])
        print("ACCNO: " + atm_data[3])
        print("BALANCE: {0:.2f}\n".format(balance))
        atm_continue()

    elif user_input == "deposit":
        notes_deposit = []
        for i in range(len(notes)):
            input("How many {}'s? ".format(notes[i]))
            notes_deposit.append(i)

        if any(x < 0 for x in notes_deposit)
            print('ERROR: Invalid input, specify a positive number\n')

        else:

    elif len(user_input.split()) == 2:

        withdraw_data = user_input.split()
        withdraw_amount = float(withdraw_data[1])

        if withdraw_amount < 0:
            print("ERROR: Unable to withdraw amount, amount requested is invalid\n")
            atm_continue()

        elif withdraw_amount > balance:
            print("ERROR: Unable to withdraw amount, amount requested is greater than balance.\n")
            atm_continue()

        else:
            balance -= withdraw_amount
            print("SUCCESS: Withdrew {0:.2f} from account\n".format(withdraw_amount))
            atm_continue()
