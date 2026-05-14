

# Has the user been there the longest?
response = input("Who's been there the longest? (yes/no/tie) ")
if (response == "yes"):
    print("Proceed")
elif (response == "no"):
    print("Wait")
else: # "tie"

    # Check the outcome of Other Car Position in relation to you.
    response = input("Where is the other car?",
                     "(left, right, across) ")
    if (response == "left"):
        print("Proceed")
    elif (response == "right"):
        print("Wait")
    else: # "across"

        # Check the user's intention.
        response = input("What is your intention?",
                        "(turn left, turn right, straight) ")
        if (response == "turn left"):
            print("Proceed")
        elif (response == "turn right" or response == "straight"):
            print("Wait")
        else: # "across"

            # Check the outcome of the other car's intention.
            response = input("Other car's intention? ")
            if (response == "turn left"):
                print("Proceed")
            else: # "turn right" OR "straight"
                print("Wait")