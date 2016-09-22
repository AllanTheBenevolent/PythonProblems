# ---------- Problem : Implement a Do While Loop ----------
# Now I want you to implement a Do While loop in Python
# They always execute all of the code at least once and at
# the end check if a condition is true that would warrant
# running the code again. They have this format
# do {
#   ... Bunch of code ...
# } while(condition)

# I'll create a guessing game in which the user must chose
# a number between 1 and 10 of the following format
'''
Guess a number between 1 and 10 : 1
Guess a number between 1 and 10 : 3
Guess a number between 1 and 10 : 5
Guess a number between 1 and 10 : 7
You guessed it
'''

secretNumber = 7

while True:
    guess = int(input("Guess a number bewtween 1 and 10:"))

    if guess == secretNumber:
        print("you guessed it!")
        break
    else:
        print("Guess again!")

# ---------- PROBLEM : SECRET STRING ----------
# Receive a uppercase string and then hide its meaning by turning
# it into a string of unicodes
# Then translate it from unicode back into its original meaning

norm_string = input("Enter a string to hide in uppercase:")
secret_string = ""
# Cycle through each character in the string
for char in norm_string:
    # Store each character code in a new string
    secret_string += str(ord(char))

print("Secret Message :", secret_string)

norm_string = ""

# Cycle through each character code 2 at a time by incrementing by
# 2 each time through since unicodes go from 65 to 90
for i in range(0, len(secret_string) - 1, 2):
    # Get the 1st and 2nd for the 2 digit number
    char_code = secret_string[i] + secret_string[i + 1]

    # Convert the codes into characters and add them to the new string
    norm_string += chr(int(char_code))

print("Original Message :", norm_string)

# ---------- SUPER AWESOME MIND SCRAMBLING PROBLEM ----------
# Make the above work with upper and lowercase with 1 addition and
# 1 subtraction

# Add these 2 changes

# secret_string += str(ord(char) - 23)

# norm_string += chr(int(char_code) + 23)

# ---------- PROBLEM : ACRONYM GENERATOR ----------
# You will enter a string and then convert it to an acronym
# with uppercase letters like this
'''
Convert to Acronym : Random Access Memory
RAM
'''
#Request for string
orig_string = input("Convert to Acronym : ")
#Convert string to all uppercase
orig_string = orig_string.upper()

#Convert string into a list
list_of_words =orig_string.split()

#Cycle through the list to grab first index(char) of each word
for word in list_of_words:
    print(word[0], end ="")


# ---------- MAKE A isfloat FUNCTION ----------
# There is no way to check if a string contains a float
# so let's make one by defining our own function

# Functions allow use to avoid repeating code
# They can receive values (attributes / parameters)
# They can return values

# You define your function name and the names for the values
# it receives like this

def isfloat(str_val):
    try:

        # If the string isn't a float float() will throw a
        # ValueError
        float(str_val)

        # If there is a value you want to return use return
        return True
    except ValueError:
        return False


pi = 3.14

# We call our functions by name and pass in a value between
# the parentheses
print("Is Pi a Float :", isfloat(pi))

# ---------- PROBLEM : CAESAR'S CIPHER ----------
# Receive a message and then encrypt it by shifting the
# characters by a requested amount to the right
# A becomes D, B becomes E for example
# Also decrypt the message back again

# A-Z have the numbers 65-90 in unicode
# a-z have the numbers 97-122
# You get the unicode of a character with ord(yourLetter)
# You convert from unicode to character with chr(yourNumber)

# You should check if a character is a letter and if not
# leave it as its default

# Hints
# Use isupper() to decided which unicodes to work with
# Add the key (number of characters to shift) and if
# bigger or smaller then the unicode for A, Z, a, or z
# increase or decrease by 26

# Receive the message to encrypt and the number of characters to shift
message = input("Enter your message : ")
key = int(input("How many characters should we shift (1 - 26)"))

# Prepare your secret message
secret_message = ""

# Cycle through each character in the message
for char in message:

    # If it isn't a letter then keep it as it is in the else below
    if char.isalpha():

        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key

        # If uppercase then compare to uppercase unicodes
        if char.isupper():

            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26

            # If smaller than A add 26
            elif char_code < ord('A'):
                char_code += 26

        # Do the same for lowercase characters
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26

        # Convert from code to letter and add to message
        secret_message += chr(char_code)

    # If not a letter leave the character as is
    else:
        secret_message += char

print("Encrypted :", secret_message)

# To decrypt the only thing that changes is the sign of the key
key = -key

orig_message = ""

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26

        orig_message += chr(char_code)

    else:
        orig_message += char

print("Decrypted :", orig_message)