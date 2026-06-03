# Prompt for a positive number.
number = int(input("Please enter a positive number: "))

# Initialize sum.
sum = 0

print("#\tnumber\tsum\tcount")
print(f"A\t{number}\t{sum}\t/")

# Count it up.
for count in range(1, number):
    print(f"B\t{number}\t{sum}\t{count}")
    sum += count        # D
    print(f"C\t{number}\t{sum}\t{count}")


# Report the result.
print(f"D\t{number}\t{sum}\t/")
print("The sum is:", sum)
#__________________________________________________________________________________________#
def binary_search(array, search):
    start_index = 0
    end_index = len(array) - 1

    print(f"#\tstart_index\tend_index\tsearch\tarray[middle_index]\tarray")
    print(f"A\t{start_index}\t\t{end_index}\t\t{search}\t/\t\t\t{array}")

    while start_index <= end_index:
        print(f"B\t{start_index}\t\t{end_index}\t\t{search}\t/\t\t\t{array}")
        
        middle_index = (start_index + end_index) // 2
        print(f"C\t{start_index}\t\t{end_index}\t\t{search}\t{array[middle_index]}\t\t\t{array}")

        if array[middle_index] == search:
            print(f"D\t{start_index}\t\t{end_index}\t\t{search}\t{array[middle_index]}\t\t\t{array}")
            return True
        
        if search > array[middle_index]:
            print(f"E\t{start_index}\t\t{end_index}\t\t{search}\t{array[middle_index]}\t\t\t{array}")
            start_index = middle_index + 1
        else:
            print(f"F\t{start_index}\t\t{end_index}\t\t{search}\t{array[middle_index]}\t\t\t{array}")
            end_index = middle_index - 1
    
    return False

print(binary_search([2, 4, 5, 7, 7, 8, 10], 6))
