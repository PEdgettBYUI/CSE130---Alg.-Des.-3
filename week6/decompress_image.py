# 1. Name:
#      Patrick T. Edgett
# 2. Assignment Name:
#      Lab 06: Image (de)Compression
# 3. Assignment Description:
#      This program decompresses data from a JSON
#       file and outputs an image using ASCII characters.
# 4. Algorithmic Efficiency
#      The algorithm uses O(n^2) time complexity.
#       This is because the decoding process requires us to go through every
#       value in a 2D array, and we need to repeat this process to
#       display the image; both of which must use a nested for loop.
# 5. What was the hardest part? Be as specific as possible.
#      As I was working on the program the biggest issue I ran into was
#       during the testing phase. My design was pretty solid overall, but
#       I seem to have some misunderstanding of how searching a 2D array works.
#       Initially there was a separate variable called row_position tracking
#       what row or column was being decoded, but for some reason it only
#       produced this straight line when the image was displayed. I'm not sure
#       why changing all instances of row_position to row_index corrected
#       this issue, but it has.
#       The second issue I encountered involves the "swap_color()" function,
#       made to make pixel color changing easier. Initially, the function
#       did not ever swap colors. I checked the debugger and traced the
#       variables through the function, and it did appear to be working. I
#       realized I should just make it return the result and assign it to the
#       pixel instead of just calling it and moving on, which seemed to fix it.
# 6. How long did it take for you to complete the assignment?
#      -total time in hours: 1.5hr + Recording: 0.5hr

import json

def read_data_from_json(filename):
    try:
        with open(filename, "rt") as file_handle:
            file_data = file_handle.read()
            json_data = json.loads(file_data)
            return json_data
    except:
        print("Unable to open file " + filename + ".")

def swap_color(pixel, on_val, off_val):
    try:
        if pixel == on_val:
            pixel = off_val
        elif pixel == off_val:
            pixel = on_val
    except:
        print(f"\n'{pixel}' does not match either color.\n")
    return pixel

pixel_on = "\u25A0"
pixel_off = " "


# "Start" of "Main program."
print("\nWelcome to the Image decompressor.\n")

# Reminder: Currently needs the path to be: "week6/[name of file].json"
file_path = input("Type the filepath you want to open: ")

raw_data = read_data_from_json(file_path)

number_of_rows = raw_data["num_rows"]
num_of_columns = raw_data["num_columns"]
compressed_data = raw_data["data"]


# Initialize the 2-dimensional array.
decoded_image = []
for row_index in range(number_of_rows):
    decoded_image.append([])

# Decompress the data in each column then move to the next row.
for column_index in range(num_of_columns):
    # Reset the row_index to 0 for the next column.
    row_index = 0
    # Reset the pixel_color value to "On"
    pixel_color = pixel_on

    # Check each row index in a given column and decode every value found.
    # For every value found, append that many characters to the decoded list.
    # After the value is decoded, swap the color of pixel_color and repeat
    #  until at the end of the column, then repeat on the next column.
    for row_data in compressed_data[column_index]:
        for compressed_value in range(row_data):
            if pixel_color == pixel_on:
                decoded_image[row_index].append(pixel_on)
                row_index += 1
                assert row_index <= number_of_rows
            elif pixel_color == pixel_off:
                decoded_image[row_index].append(pixel_off)
                row_index += 1
                assert row_index <= number_of_rows
            else:
                print("\n[A CRITICAL ERROR HAS OCCURED.]\n")
                break
        pixel_color = swap_color(pixel_color, pixel_on, pixel_off)

# Non-essential spacing, for aesthetic purposes.
print("\n\n")

# Display the final image.
for row in decoded_image:
    for pixel in row:
        print(pixel, end='')
    print()
print()
