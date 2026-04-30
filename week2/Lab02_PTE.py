# 1. Name:
#      Patrick T. Edgett
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program is a simple authenticator using names and quotes from Monty Python and The Holy Grail for the username and password.
#       This excercise also exists to allow us to practice interacting with JSON objects, using a file called Lab02.json to store the usernames and passwords in a dictionary.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

# Stores filepath of the authenticator dictionary
file_path = "week2/Lab02.json"

# NOTE: While loop used for demonstration video purposes
# NOTE: type 'exit' as username input to end program
username_user_input = "blank"
while username_user_input != "exit":
    try:
        with(open(file_path, "r")) as file:
            data_text = file.read() # <-- The JSON is converted to a raw string

            ## TEST prints
            print("JSON as string:", data_text)
    
    except Exception as e:
        print(f"Unable to open file {file_path}: {e}")
    

    # Prompt for Username
    username_user_input = input("Enter your Username: ")

    # Prompt for Password

    # Check if Username and Password match the correct entries in the linked-list