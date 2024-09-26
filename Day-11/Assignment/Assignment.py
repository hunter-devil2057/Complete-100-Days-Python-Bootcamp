'''
- Create an empty dictionary named my_dict.
- Prompt the user to enter the name and age of five people.
- Store the name as the key and the age as the value in the dictionary.
- Print the dictionary.
- Find and print the following:
    - The number of people in the dictionary.
    - The sum of all ages.
    - The average age of the people.
    - The oldest person's name and age.
    - The youngest person's name and age.
'''

# Creating an Empty Dictionary named 'my_dict'
my_dict={}

# Prompting the user to Enter the name and age of five people
for i in range(5):
    name=input(f"Enter the Name of Person {i+1}:")
    age=int(input(f"Enter the Age of {name}:"))

    # Storing the name as the key and age as the value in the dictionary
    my_dict[name]=age

# Print the Dictionary after Loop Completely Ends
print(my_dict)

# Finding out the number of people in the Dictionary
print("Number of people: ", len(my_dict))

# Finding out the sum of all ages
sumAges=sum(my_dict.values())
print("Sum of all ages: ", sumAges)

# Average of ages of all the peoples
avgAges=(sumAges/len(my_dict))
print("Average of all ages: ", avgAges)

# Oldest Person Name and Age
oldAge=max(my_dict.values())
oldName=max(my_dict, key=my_dict.get)
print("Oldest Person: ", oldName)
print(f"{oldName}: {oldAge} years old")

# Youngest Person Name and Age
youngAge=min(my_dict.values())
youngName=min(my_dict, key=my_dict.get)
print("Youngest Person: ", youngName)
print(f"{youngName}: {youngAge} years old")