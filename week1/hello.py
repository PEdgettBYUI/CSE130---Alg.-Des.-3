# Display "Hello world".
print("Hello world.")

# Display "This is CSE 130" but 130 is an integer
print("This is CSE", 130)
print(f"This is CSE {130}")

# Display 2, 4, 6; where 2, 4, 6 are part of a list
int_list = [2, 4, 6]
for number in int_list:
    print(number)

# Prompt the user for their age
age = int(input("What is your age? "))
print(f"Your age is: {age}")

# Display the values from 0-9 using a loop
print("For Loop Version")
for i in range(10):
    print(i)

print("While Loop Version")
dis_val = 1
while dis_val <= 9:
    print(dis_val)
    dis_val += 1


# Loop until the user says stop
usr_inp = input("Should I stop? ")
while usr_inp != "stop":
    usr_inp = input("Should I stop? ")
print("I have stopped.")