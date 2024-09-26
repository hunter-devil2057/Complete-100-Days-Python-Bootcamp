# Arithmetic Operations
'''
Create three variables num1, num2, and num3 with values 10, 5, and 3 respectively.

Perform the following arithmetic operations and store the results in variables:

Addition: Add num1 and num2 and then add num3 to the result. Store the final result in a variable named add_result.

Subtraction: Subtract num2 from num1 and then subtract num3 from the result. Store the final result in a variable named sub_result.

Multiplication: Multiply num1 by num2 and then multiply the result by num3. Store the final result in a variable named mul_result.

Division: Divide num1 by num2 and then divide the result by num3. Store the final result in a variable named div_result.

Exponentiation: Raise num1 to the power of num2 and then raise the result to the power of num3. Store the final result in a variable named exp_result.

Print the results of all the operations.
'''
num1=10; num2=5; num3=3

add_result=num1+num2+num3
print(add_result)

diff=num1-num2
sub_result=diff-num3
print(sub_result)

mul_result=num1*num2*num3
print(mul_result)

res=num1/num2
div_result=res/num3
print(div_result)

exp_result=((num1**num2)**num3)
print(exp_result)