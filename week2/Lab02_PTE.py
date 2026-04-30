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

            # print("JSON as string:", data_text)   # TEST print

            # Convert raw string into a python dictionary
            data_dictionary = json.loads(data_text)
    
            # Split the dictionary into two linked-lists
            username_dictionary = data_dictionary["username"]
            password_dictionary = data_dictionary["password"]
    
    except Exception as e:
        print(f"Unable to open file {file_path}: {e}")
    

    # Prompt for Username
    username_user_input = input("Enter your Username: ")

    # Prompt for Password
    password_user_input = input("Enter your Password: ")

    # Check if Username and Password match the correct entries in the linked-list
    if username_user_input in username_dictionary:
        # Obtain username's index for verification
        index = username_dictionary.index(username_user_input)

        # Check if the user provided password matches the password stored at the matching index in the password_dictionary
        if password_user_input == password_dictionary[index]:
            print("You are authenticated.")
        else:
            print("You are not an authorized user in this system.")
    else:
        print("You are not an authorized user in this system.")
    print()