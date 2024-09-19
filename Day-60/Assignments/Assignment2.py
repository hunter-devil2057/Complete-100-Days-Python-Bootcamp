# Write A Python Program To Check Alpha Character, Whether Vowel Or Consonant.
charIn=input("Enter a Single Character: ")
# charIn=input("Enter a Single Character: ")[0]
#Here, [0] captures only the first character when an string is entered

# Checking the length of the input string 
if(charIn.isalpha() and len(charIn)==1):
    # isalpha(): checks whether the input is in alphabet
    # (len(charIn)==1): checks the length of the input, char has, length 1

    # Checking if the character is Vowel 
    if charIn in 'aeiou':
        print(f"{charIn} is Vowel Character")

    else:   #if the character is Consonant
        print(f"{charIn} is Consonant Characters")
        
else:       #if the input is not character
    print("Input Invalid!!!")