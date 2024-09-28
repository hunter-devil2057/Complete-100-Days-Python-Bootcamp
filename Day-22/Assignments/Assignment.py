# Membership Operator
'''
Create a list named my_list containing the elements 1, 2, 3, 4, and 5.
Prompt the user to enter a number.
Check if the entered number is present in my_list using membership operators.
Print the result.
'''

my_list=[1, 2, 3, 4, 5]
numCheck=int(input("Enter a Number: "))
if(numCheck in my_list):
    print(numCheck, "is available")
    print(my_list)
else:
    print(numCheck, "is not available")