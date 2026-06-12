# 1. Name:
#      Patrick T. Edgett
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program is a demonstration of a selection sort algorithm of O(n^2)
#       efficiency, and includes various asserts that cover potential bugs.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      50mins + 

import json

def read_data_from_json(filename):
    try:
        with open(filename, "rt") as file_handle:
            file_data = file_handle.read()
            json_data = json.loads(file_data)
            return json_data
    except:
        print("Unable to open file " + filename + ".")

file_path = input("Type the name of the file you want to open: ")
raw_json_data = read_data_from_json("week8/" + file_path)
array_of_strings = raw_json_data["array"]
# print(array_of_strings[2])

# # Reduces array size each successive iteration
# FOR end_point = 1 … (size of array - 1):
for end_point in range(0, len(array_of_strings) - 1):
    assert len(array_of_strings) >= 0
# 	# Set the first comparison item to the first index
    biggest_index = 0
# 	# Check each index to the current “end point” for the largest item
#   FOR index = 1 … ((size of array) - end_point):
    for current_index in range(1, len(array_of_strings) - end_point):
#       IF (array[index] > [biggest_item]):
        if (array_of_strings[current_index] > array_of_strings[biggest_index]):
            biggest_index = current_index
# # Swap the current largest item’s index and the current “end point”
#   Swap(array[biggest_item], array[(size of array - end_point)
    swap_index = len(array_of_strings) - 1 - end_point
    array_of_strings[biggest_index], array_of_strings[swap_index] = (
    array_of_strings[swap_index], array_of_strings[biggest_index])
    print(array_of_strings)
# # The final output should be sorted from least to greatest
# print(array_of_strings)

print(f"The values in {file_path} are:")
for i in range(0, len(array_of_strings)):
    print(f"    {array_of_strings[i]}")