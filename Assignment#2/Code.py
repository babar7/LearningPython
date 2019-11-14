# 1. Write a program which takes 5 inputs from user for different subject’s
# marks, total it and generate mark sheet using grades ?
# 2. Write a program which take input from user and identify that the given
# number is even or odd?
# 3. Write a program which print the length of the list?
# 4. Write a Python program to sum all the numeric items in a list?
# 5. Write a Python program to get the largest number from a numeric list.
# 6. Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are
# less than 5.


# 1. Write a program which takes 5 inputs from user for different subject’s
# marks, total it and generate mark sheet using grades ?
# ==================================START==============================================

print("Please write roundoff number in integer form ")
english = int(input("Please enter your english marks :: "))
maths = int(input("Please enter your maths marks :: "))
computer = int(input("Please enter your computer marks :: "))
science = int(input("Please enter your science marks :: "))
physics = int(input("Please enter your physics marks :: "))
total = english + maths + computer + science + physics
percentage = (total/500) * 100

if percentage >= 80 and percentage <= 100:
    print("Your grade is A` with  ", percentage, "%")
elif percentage >= 70 and percentage < 80:
    print("Your grade is A with ", percentage, "%")
elif percentage >= 60 and percentage < 70:
    print("Your grade is B with ", percentage, "%")
elif percentage >= 50 and percentage < 60:
    print("Your grade is C with ", percentage, "%")
elif percentage > 0 and percentage < 50:
    print("Sorry you are fail and your percentage is ", percentage, "%")
else:
    print("Wrong input")

# ----------------------------------END-------------------------------------------------
