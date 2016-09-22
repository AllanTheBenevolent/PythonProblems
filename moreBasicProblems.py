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

