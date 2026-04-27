# Hello world.
print("Hello world")

# Helfrich was born in 1971, as an int
helfrich_birth_year = 1971
print(f"Brother Helfrich was born in {helfrich_birth_year}")

# I was born in the year 2000, as an int
print(f"I was born in {2000}")

# Prompt for name, then display usr_name
usr_name = input("What is your name? ")
print(f"Your name is: {usr_name}")

# Prompt for birth year, then display their current age in years
usr_birth_year = int(input("What year were you born? "))
year_now = 2026
print("You will turn", year_now - usr_birth_year, "this year.")

# Python List reminder - should return 6
data = [2, 4, 6, 8]
print(data[2])

# data = [2, 2, 2, 2, 2, 2, 5, 6] # List
data = {2, 2, 6, 2, 2, 2, 5, 2} # Sets cannot have repeated data and are always sorted, so this will show {2, 5, 6}
print(data)

# Dictionary aka "Hash Map"
data = {"Police":911, "Operator":0, "Jenny":8675309}
data["Police"]