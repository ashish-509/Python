
# Try and Except : We can use the try and except blocks to prevent your program from crashing due to exceptions.

# using Try- except 
try:
    result = 10 / 0 # Attempting to divide 10 by 0
    print('Divided by 0')  # This line is not executed as execution of program goes to except block when encountered exception in above line
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")


a = 1

try:
    b = int(input("Please enter a number to divide a "))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")

