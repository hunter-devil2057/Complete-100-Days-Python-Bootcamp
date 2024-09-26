# Relational Operator
'''
Create two variables num1 and num2 with values 10 and 5 respectively.

Perform the following relational operations and store the results in variables:

Greater Than: Check if num1 is greater than num2 and store the result in a variable named greater_than.

Less Than: Check if num1 is less than num2 and store the result in a variable named less_than.

Equal To: Check if num1 is equal to num2 and store the result in a variable named equal_to.

Not Equal To: Check if num1 is not equal to num2 and store the result in a variable named not_equal_to.

Greater Than or Equal To: Check if num1 is greater than or equal to num2 and store the result in a variable named greater_than_equal_to.

Less Than or Equal To: Check if num1 is less than or equal to num2 and store the result in a variable named less_than_equal_to.

Print the results of all the operations.
'''

num1=10; num2=5
# Greater Than
if(num1>num2):
    greater_than=num1
else:
    greater_than=num2
print("Greater Number is: ", str(greater_than))

# Less Than 
if(num1<num2):
    less_than=num1
else:
    less_than=num2
print("Lesser Number is: ", str(less_than))

# Equal to 
if(num1==num2):
    equal_to=num1
    print("Both Numbers are Equal")
else:
    print("Both Numbers are not Equal")

# Not Equal to
if(num1!=num2):
    not_equal_to=num1
    print("Both Numbers are not Equal")
else:
    print("Both Numbers are Equal")

# Greater Than or Equal to 
if(num1>=num2):
    greater_than_equal_to=num1
    print(greater_than_equal_to+" is greater than or equal to "+num2)

# Lesser Than or Equal to 
if(num1<=num2):
    less_than_equal_to=num1
    print(less_than_equal_to+" is lesser than or equal to "+num2)