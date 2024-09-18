# Factorial of a Number
def Factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*Factorial(num-1)
num=int(input("Enter a Number: "))

if(num<0):
    print("Factorial of Negative Number doesn't Exists.")
else:
    print("Factorial: ",Factorial(num))