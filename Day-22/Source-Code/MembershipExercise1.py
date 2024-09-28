# Write a Python Program to find Occurrence of Specific Color from a List
ColorList=["red", "green", "gray", "pink", "black", "white"]
colorName=input("Enter a Color Name: ").lower()

if(colorName in ColorList):
    print("Color is present in the List.")
    print(ColorList)
else:
    print("Color is not present in the List.")
    print(ColorList)