'''
Define two variables num1 and num2 with values 10 and 20 respectively.

Perform the following operations:

Implicit conversion: Add num1 and num2 and store the result in a variable named result_implicit.

Explicit conversion: Convert num1 to a string and concatenate it with the string " + " and then with num2 converted to a string. Store the result in a variable named result_explicit.

Print both result_implicit and result_explicit.
'''

num1=10; num2=20
result_implicit=num1+num2

a=str(num1); b=str(num2)
result_explicit=a+b

print(result_implicit)
print(result_explicit)
