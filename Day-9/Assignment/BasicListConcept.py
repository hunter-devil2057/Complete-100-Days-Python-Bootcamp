# Create an empty list
my_list = []

# Prompt the user to enter five numbers and store them in the list
for i in range(5):
    number = float(input(f"Enter number {i+1}: "))
    my_list.append(number)

# Print the list
print("The list is:", my_list)

# Find and print the length of the list
list_length = len(my_list)
print("Length of the list:", list_length)

# Find and print the sum of all the numbers in the list
list_sum = sum(my_list)
print("Sum of all numbers in the list:", list_sum)

# Find and print the largest number in the list
max_number = max(my_list)
print("Largest number in the list:", max_number)

# Find and print the smallest number in the list
min_number = min(my_list)
print("Smallest number in the list:", min_number)
