# Write a Python Program to find Occurrence of Specific Student Name From a Tuple
studentName=("John", "Harry", "Robert", "Stephen", "Manish")

nameInput=input("Enter Student Name:").capitalize()
if(nameInput in studentName):
    print("Student Name "+nameInput+" is available in the record")
else:
    print("Student Name "+nameInput+" is not available in the record.")