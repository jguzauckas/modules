# Import our three modules here!
from calendar import c
import math
import random
from datetime import datetime

# Math
# Ask the user to enter a float number and save it to a variable.  Then,
# calculate the ceiling and floor of their number and print the results.
user_float = float(input("Enter a decimal number: "))
print(f"The floor of your number is {math.floor(user_float)}")
print(f"The ceiling of your number is {math.ceil(user_float)}")

# Create a list containing all of your scores from assignments in this
# class from this quarter.  Calculate the sum and product of all of those
# grades and print the results with nice formatting.
scores = [5, 10, 5, 5, 3, 16, 20]  # Your list will be longer than this
print(f"The sum of your scores is {math.fsum(scores)}")
print(f"The product of your scores is {math.prod(scores)}")

# Have the user enter an integer from 1 to 50 and save it to a variable.
# Then, calculate the factorial of their number and print the result.
user_integer = int(input("Enter an integer from 1 to 50: "))
print(f"The factorial of {user_integer} is {math.factorial(user_integer):,}")

# Random
# Generate a random float and save it to a variable.  Print out to the
# user that their current grade is that random number formatted as a
# percentage with 3 decimal places.
random_float = random.random()
print(f"Your current grade in this class is {random_float:.3%}")

# Use randint to flip a coin (think: how many options does a coin flip
# have?).  Depending on the random value, either print heads or tails.
coin_flip = random.randint(1, 2)
if coin_flip == 1:
    print("You got heads!")
else:
    print("You got tails!")

# Datetime
# Create a variable that stores a datetime object with the current time.
# Print out the current datetime.
current_datetime = datetime.now()
print(f"The current datetime is {current_datetime}")

# Create a variable that stores your birthday from this year as a datetime
# object.  Print out your birthday.
my_birthday = datetime(2022, 8, 5)
print(f"My birthday is {my_birthday}")

# Use a comparison of those two variables to state whether or not your
# birthday has happened yet this year.
if current_datetime > my_birthday:
    print("My birthday has already happened this year")
else:
    print("My birthday is coming up still this year!")
