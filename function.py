# ---------- PROBLEM : SOLVE FOR X ----------
# Make a function that receives an algebraic equation like
# x + 4 = 9 and solve for x
# x will always be the 1st value received and you only
# will deal with addition

# Receive the string and split the string into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()
    #convert the strings into ints
    num1, num2 = int(num1), int(num2)

    #Convert the result into a string and join (concatenate)
    # it to the string "x = "
    return "x = " + str(num2 - num1)

print(solve_eq("x + 4 = 9"))

# We need this module for our program
import math


# Functions allow us to avoid duplicate code in our programs

# Aside from having to type code twice duplicate code is bad
# because it requires us to change multiple blocks of code
# if we need to make a change

# ---------- OUR FUNCTIONS ----------

# This routes to the correct area function
# The name of the value passed doesn't have to match
def get_area(shape):
    # Switch to lowercase for easy comparison
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")


# Create function that calculates the rectangle area
def rectangle_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width : "))

    area = length * width

    print("The area of the rectangle is", area)


# Create function that calculates the circle area
def circle_area():
    radius = float(input("Enter the radius : "))

    area = math.pi * (math.pow(radius, 2))

    # Format the output to 2 decimal places
    print("The area of the circle is {:.2f}".format(area))


    # ---------- END OF OUR FUNCTIONS ----------