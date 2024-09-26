# Basic Set Operations
'''
Create two sets named set1 and set2 containing integer values.

Prompt the user to enter five numbers separated by space and store them in set1.

Prompt the user to enter five more numbers separated by space and store them in set2.

Print both sets.

Find and print the following:
    The union of set1 and set2.
    The intersection of set1 and set2.
    The difference between set1 and set2.
    The symmetric difference between set1 and set2.
'''
# Prompt the user to enter five numbers separated by space for set1
set1 = set(map(int, input("Enter five numbers for set1, separated by spaces: ").split()))

# Prompt the user to enter five more numbers separated by space for set2
set2 = set(map(int, input("Enter five numbers for set2, separated by spaces: ").split()))

# Print both sets
print("\nSet1:", set1)
print("Set2:", set2)

# Find and print the union of set1 and set2
union_set = set1.union(set2)
print("\nUnion of set1 and set2:", union_set)

# Find and print the intersection of set1 and set2
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Find and print the difference between set1 and set2 (set1 - set2)
difference_set = set1.difference(set2)
print("Difference between set1 and set2 (set1 - set2):", difference_set)

# Find and print the symmetric difference between set1 and set2
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference between set1 and set2:", symmetric_difference_set)
