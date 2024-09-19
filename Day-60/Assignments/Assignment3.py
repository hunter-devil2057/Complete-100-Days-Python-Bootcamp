# Write a Python program get name of week and show “Holiday” if user input Sunday
# Receiving Days of the Week
daysWeek=input("Enter the name of the Day:").capitalize()

# checking the input
if daysWeek=="Sunday":
    print("It's Holiday")
else:
    print(f"{daysWeek} is not a Holiday.")