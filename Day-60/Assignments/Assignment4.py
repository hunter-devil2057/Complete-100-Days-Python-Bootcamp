# Write Python Program To Get A Username From The User That Should Have Alphanumeric Characters, Then Pass That Username To Function As Parameter, To Display That Username
def userName(username):
    print(f"Your UserName is: {username}")

# Get Input from the User. 
username=input("Enter your UserName(Use AlphaNumeric Characters Only):")

if username.isalnum(): 
    userName(username)
else:
    print("Invalid UserName. Please use only Alphanumeric Characters.")