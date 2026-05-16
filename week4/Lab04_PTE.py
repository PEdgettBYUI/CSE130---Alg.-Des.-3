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

# Function to display the 4 possible outputs for Purchasing a hotel.
def purchase_results(price, houses_on_NC, houses_on_PC, total_houses):
    # Find out how many houses are needed for North Carolina
    houses_for_NC = 4 - houses_on_NC
    # Find out how many houses are needed for Pacific Avenue
    houses_for_PC = 4 - houses_on_PC
    print(f"\nThis will cost ${price}.")
    print(f"    Purchase 1 hotel and {total_houses} house(s).")
    print("    Put 1 hotel on Pennsylvania and return any houses to the bank.")
    if(houses_for_NC > 0):
        print(f"Put {houses_for_NC} house(s) on North Carolina.")
    if(houses_for_PC > 0):
        print(f"Put {houses_for_NC} house(s) on Pacific.")

# Initialize variables.
total_houses_on_green = 0
houses_on_PA = 0
houses_on_NC = 0
houses_on_PC = 0
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
    user_input = str(input("Do you own all the green properties? (y/n) ")).lower()
    if (user_input == "n"):
        print("\nYou cannot purchase a hotel until you own" \
        "all the properties of a given color group.")
        break
        


    # Prompt the user to enter what is currently on Pennsylvania Avenue.
    user_input = int(input("What is on Pennsylvania Avenue? " \
        "(0:nothing, 1:one house, ... 5:a hotel) "))

    # If the user_input variable is between 0 and 5, 
    # add the value to the total_houses_on_green counter
    if(user_input > 0 or user_input < 5):
        houses_on_PA += user_input


    # If 5, output: Already has Hotel.
    if (user_input == 5):
        print("\nYou cannot purchase a hotel if the property already has one.")
        break


    # Prompt the user to enter what is currently on Pacific Avenue.
    user_input = int(input("What is on Pacific Avenue? " \
        "(0:nothing, 1:one house, ... 5:a hotel) "))
    
    # If the user_input variable is between 0 and 5, 
    # add the value to the total_houses_on_green counter
    if(user_input > 0 or user_input < 5):
        houses_on_PC += user_input

    # If 5, output: Swap PC Hotel.
    if (user_input == 5):
        print("\nSwap Pacific's hotel with Pennsylvania's 4 houses.")
        break

    # Prompt the user to enter what is currently on North Carolina Avenue.
    user_input = int(input("What is on North Carolina Avenue? " \
        "(0:nothing, 1:one house, ... 5:a hotel) "))
    
    # If the user_input variable is between 0 and 5, 
    # add the value to the total_houses_on_green counter
    if(user_input > 0 or user_input < 5):
        houses_on_NC += user_input

    # If 5, output: Swap: NC Hotel.
    if (user_input == 5):
        print("\nSwap North Carolina's hotel with Pennsylvania's 4 houses.")
        break

    # Prompt the user to enter how many hotels are available for purchase from the bank.
    hotels_in_bank = int(input("How many hotels are there to purchase? "))
    # If hotels_in_bank < 1, output: No Hotels.
    if (hotels_in_bank < 1):
        print("\nThere are not enough hotels available for purchase at this time.")
        break


    # Calculate the total houses on green.
    total_houses_on_green = houses_on_PA + houses_on_NC + houses_on_PC
    # Calculate the number of houses needed to buy 1 hotel for PA Avenue.
    needed_houses = 12 - total_houses_on_green
    #  Calculate the amount of cash needed to buy 1 hotel on PA Avenue.
    cash_needed = (200 * needed_houses) + 200

    
    # Prompt the user to confirm whether the bank has enough houses for sale.
    houses_in_bank = int(input("How many houses are there to purchase? "))
    # If houses_in_bank < needed_houses, output: Not Enough Houses.
    if (houses_in_bank < needed_houses):
        print("\nThere are not enough houses available for purchase at this time.")
        break

    # Prompt the user to enter how much cash they have available.
    cash_available = int(input("How much cash do you have to spend? "))
    # If cash < (200 * needed_houses), the user cannot afford the purchase.
    if(cash_available < cash_needed):
        print("\nYou do not have sufficient funds to purchase a hotel at this time.")
        break

    # Display the final purchase results
    purchase_results(cash_needed, houses_on_NC, houses_on_PA, total_houses_on_green)
