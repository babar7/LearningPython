# 1. Write a Python program to print the following string in a specific format
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# Twinkle, twinkle, little star,
# How I wonder what you are

from math import pi
import platform
import datetime
import sys
from datetime import date

# ==================================START==============================================

line1 = "Twinkle, twinkle, little star, \n"
line2 = "      How I wonder what you are! \n"
line3 = "            Up above the world so high, \n"
line4 = "            Like a diamond in the sky. \n"
poem = line1 + line2 + line3 + line4 + line1 + line2
print(poem)

# ----------------------------------END-------------------------------------------------


# 2. Write a Python program to get the Python version you are using
# ==================================START==============================================

# For prints the full version information string.
# import sys
print(sys.version)


# For getting version only
# import platform
print(platform.python_version())

# ----------------------------------END------------------------------------------------

# 3. Write a Python program to display the current date and time.
# ==================================START==============================================
# import datetime
currentTimeAndDate = datetime.datetime.now()
print(currentTimeAndDate)

# Gatting only today's date
date = datetime.date.today()
print(date)

# Getting only date you can also write this
# from datetime import date
today = date.today()
print(today)

# Current Month Year and Day
# from datetime import date
print(today.year)
print(today.month)
print(today.day)

# ----------------------------------END------------------------------------------------

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
# ==================================START==============================================

# Area of a circle is A = πr2
# from math import pi
radius = float(input("Please write the radius of the circle : "))
print("The area of the circle with radius " +
      str(radius) + " is: " + str(pi * radius ** 2))
# Usring str to convert float to string for concatination

# You can also print string with number without using str
print("The area of the circle with radius ",
      radius, " is: ", (pi * radius ** 2))

# ----------------------------------END------------------------------------------------

# 5. Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.
# ==================================START==============================================

# There is no build in reverse function in python but there is many way to do this, the easiest one i think is
firstName = input("Please enter your first name : ")
lastName = input("Please enter your last name : ")
fullName = firstName + lastName
reversedName = fullName[::-1]
print(reversedName)

# Having space between them
stringName = 'Python'  # initial string
# .join() method merges all of the characters resulting from the reversed iteration into a new string
reversedStr = ' '.join(reversed(stringName))
print(reversedStr)  # print the reversed string

# ----------------------------------END------------------------------------------------

# 6. Write a python program which takes two inputs from user and print them
# addition
# ==================================START==============================================

firstNumber = input("Please enter first 'integer' value to add : ")
secondNumber = input("Please enter second 'integer' value to add : ")
result = int(firstNumber) + int(secondNumber)
print(result)

# ----------------------------------END------------------------------------------------
