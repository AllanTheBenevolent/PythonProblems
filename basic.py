#Basic program problems solved in python for basic practice. Heavily commented for easy to read step by step

#************PROBLEM: Print odds from 1 to 20:****************

#Use for loop range, if and modulus to print out the numbers

#Use for to loop through list from 1 to 21

for i in range(1, 21):

#use modulus to check if number is odd
#Proceed to print odd.
    if ((i % 2) != 0):
        print ("i = ", i)


#*********PROBLEM: Compounding Interest:***************

#Have user enter investment amount and expected interest
#Each year their investment will increase by their investment + their investment*the interest rate
#Print out earnings after a inputed year period

#Ask for money invested + interst rate
money = input("How much to invest: ")
interest_rate = input("What is the interest rate:")
yearsProjected = input("Project the number of years you want to caclulate earnings for:")

#Convert value to a float(Inputed value must be made to float for accuracy)
money = float(money)

#Convert value to a float and round percentage by 2 digits
interest_rate = float(interest_rate) * .01

#Convert value to integer for years
yearsProjected = int(yearsProjected)
#cycle through inputed years

for i in range(yearsProjected):
    money = money +(money*interest_rate)

#Convert back to string
#{:.2f} just means to print float to 2 digit. {} just references the format
print("Investment after {} years: {:.2f}".format(yearsProjected, money))

# ---------- PROBLEM : DRAW A PINE TREE ----------
# For this problem I want you to draw a pine tree after asking the user
# for the number of rows. Here is the sample program

'''
How tall is the tree : 5
    #
   ###
  #####
 #######
#########
    #
'''
#Sugested: Use a while loop and 3 for loops
#Some quick notes:
#This is the number of spaces and hashes for the tree
# 4 - 1
# 3 - 3
# 2 - 5
# 1 - 7
# 0 - 9
# Spaces before stump = Spaces before top

# So what we'll need to is
# 1. Decrement spaces by one each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash

#Ask user for # of rows for tree
tree_height = input("How tall is the tree :")
#Convert to integer
tree_height = int(tree_height)

#Get starting spaces for top of the tree
spaces = tree_height -1

#Get hash to start incrementation. Has default should start as 1 to symbolize top of tree
hashes = 1
#Save stump spaces til later. Since its the same as the top.
stump_spaces = tree_height -1

#Make sure right number of rows are printed
while tree_height !=0:
    #print spaces
    # end = ""Means newline won't be added
    for i in range(spaces):
        print(' ', end="")
    #print the hashes
    for i in range(hashes):
        print('#', end ="")
    #Newline print after each row

    print()
    #Decrement spaces
    spaces -= 1
    #Increment hashes
    hashes +=2
    #decrement tree height each time to jumpout of loop eventually
    tree_height -=1
#Print the spaces before stump and then a hash\
for i in range(stump_spaces):
    print(' ', end="")

print("#")

