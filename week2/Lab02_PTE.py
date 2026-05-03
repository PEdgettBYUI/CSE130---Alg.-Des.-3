# 1. Name:
# Patrick T. Edgett
# 2. Assignment Name:
# Lab 02: Authentication
# 3. Assignment Description:
# This program is a simple authenticator using names and quotes from
# Monty Python and The Holy Grail for the username and password. This
# exercise also exists to allow us to practice interacting with JSON
# objects using a file called Lab02.json to store the usernames and
# passwords in a dictionary.
# 4. What was the hardest part? Be as specific as possible.
# This assignment was a good refresher on reading from a JSON file.
# I had forgotten how to convert it from a string to a dictionary at
# first, but it was simpler than I remembered. One issue I ran into was
# that the file is stored as part of a repository for the class, and I
# initially did not account for the need to supply the path during
# testing, which caused the program to crash. I added a try-except block
# to prevent that issue. I have not demonstrated the program yet, but I may
# need to re-record the demo to account for the fix.
# 5. How long did it take for you to complete the assignment?
# Approximately 1.5 hours

import json

# Stores file path of the authenticator dictionary
file_path = "week2/Lab02.json"

# NOTE: While loop used for demonstration video purposes
# NOTE: type 'exit' as username input to end program
username_user_input = "blank"
while username_user_input != "exit":
    try:
        with(open(file_path, "r")) as file:
            data_text = file.read() # <-- The JSON is converted to a raw string

            # print("JSON as string:", data_text)   # TEST print

            # Convert raw string into a Python dictionary
            data_dictionary = json.loads(data_text)
    
            # Split the dictionary into two linked lists
            username_dictionary = data_dictionary["username"]
            password_dictionary = data_dictionary["password"]
    
    except Exception as e:
        print(f"Unable to open file {file_path}: {e}")
    

    # Prompt for username
    username_user_input = input("Enter your Username: ")

    # Prompt for password
    password_user_input = input("Enter your Password: ")

    # Check if username and password match the correct entries in the linked list
    if username_user_input in username_dictionary:
        # Obtain username's index for verification
        index = username_dictionary.index(username_user_input)

        # Check if the user-provided password matches the password stored at the matching index in the password_dictionary
        if password_user_input == password_dictionary[index]:
            print("You are authenticated.")
        else:
            print("You are not an authorized user in this system.")
    else:
        print("You are not an authorized user in this system.")
    print()