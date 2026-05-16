# 1. Name:
#      Patrick T. Edgett
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program determines if you can put a hotel on Pennsylvania Avenue.
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python?
#      Was it an aspect of the problem you are to solve?
#      Was it the instructions or any part of the problem definition?
#      Was it the submission process?
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-



# Initialize variables.
total_houses_on_green = 0
hotels_in_bank = 0
houses_in_bank = 0
cash_available = 0
cash_needed = 0

# Program introduction.
print(" Welcome to the program!\n")

start = 'y'
# NOTE: Temporary Loop using Breaks, will remove after testing concludes
while start == 'y':
    start = 'n'

    # Prompt the user to confirm whether they own all green properties.
    # If false, output: No Properties.
    user_input = str(input("Do you own all the green properties? (y/n) "))
    if (user_input == "n"):
        print("You cannot purchase a hotel until you own" \
        "all the properties of a given color group.")
        break


    # Prompt the user to enter what is currently on Pennsylvania Avenue.
    user_input = int(input("What is on Pennsylvania Avenue? " \
        "(0:nothing, 1:one house, ... 5:a hotel) "))

    # If the user_input variable is between 0 and 5, 
    # add the value to the total_houses_on_green counter
    if(user_input > 0 or user_input < 5):
        total_houses_on_green += user_input

    # If 5, output: Already has Hotel.
    if (user_input == 5):
        print("You cannot purchase a hotel if the property already has one.")
        break


    # Prompt the user to enter what is currently on Pacific Avenue.
    user_input = int(input("What is on Pacific Avenue? " \
        "(0:nothing, 1:one house, ... 5:a hotel) "))
    
    # If the user_input variable is between 0 and 5, 
    # add the value to the total_houses_on_green counter
    if(user_input > 0 or user_input < 5):
        total_houses_on_green += user_input

    # If 5, output: Swap PC Hotel.
    if (user_input == 5):
        print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
        break

    # Prompt the user to enter what is currently on North Carolina Avenue.
    user_input = int(input("What is on North Carolina Avenue? " \
        "(0:nothing, 1:one house, ... 5:a hotel) "))
    
    # If the user_input variable is between 0 and 5, 
    # add the value to the total_houses_on_green counter
    if(user_input > 0 or user_input < 5):
        total_houses_on_green += user_input

    # If 5, output: Swap: NC Hotel.
    if (user_input == 5):
        print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
        break


    # Calculate needed_houses by finding the difference.
    needed_houses = 12 - total_houses_on_green
    cash_needed = 200 * needed_houses
    # Prompt the user to enter how many hotels are available for purchase from the bank.
    hotels_in_bank = int(input("How many hotels are there to purchase? "))
    # If hotels_in_bank < 1, output: No Hotels.
    if (hotels_in_bank < 1):
        print("There are not enough hotels available for purchase at this time.")
        break

    # Prompt the user to confirm whether the bank has enough houses for sale.
    houses_in_bank = int(input("How many houses are there to purchase? "))
    # If houses_in_bank < needed_houses, output: Not Enough Houses.
    if (houses_in_bank < needed_houses):
        print("There are not enough houses available for purchase at this time.")
        break

    # Prompt the user to enter how much cash they have available.
    cash_available = int(input("How much cash do you have to spend? "))
    # If cash < (200 * needed_houses), the user cannot afford the purchase.
    if(cash_available < cash_needed):
        print("You do not have sufficient funds to purchase a hotel at this time.")
        break
