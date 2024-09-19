# Write a Python Program to get 5 number from user in array, find the maximum number
numArray=[]      #initializing empty array to store numbers

# Taking 5 Numbers from the User
for i in range(5):
    num=float(input("Enter a Number {i+1}:"))
    num.append(numArray)

maxNumbers=max(numArray)
print(f"Maximum Number in an Array: {maxNumbers}")