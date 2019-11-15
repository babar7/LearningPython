# 1. Write a program which takes 5 inputs from user for different subject’s
# marks, total it and generate mark sheet using grades ?
# ==================================START==============================================

english = float(input("Please enter your english marks :: "))
maths = float(input("Please enter your maths marks :: "))
computer = float(input("Please enter your computer marks :: "))
science = float(input("Please enter your science marks :: "))
physics = float(input("Please enter your physics marks :: "))
total = english + maths + computer + science + physics
percentage = (total/500) * 100

if(percentage > 100 or percentage < 0):
    print("Please check your input and write again")
else:
    if percentage >= 80:
        print("Your grade is A` with  ", percentage, "%")
    elif percentage >= 70:
        print("Your grade is A with ", percentage, "%")
    elif percentage >= 60:
        print("Your grade is B with ", percentage, "%")
    elif percentage >= 50:
        print("Your grade is C with ", percentage, "%")
    elif percentage >= 40:
        print("Your grade is D with ", percentage, "%")
    else:
        print("Sorry you are fail and your percentage is ", percentage, "%")

# ----------------------------------END-------------------------------------------------

# 2. Write a program which take input from user and identify that the given
# number is even or odd?
# ==================================START==============================================

numberToIdentify = int(
    input("Please enter any integer value to identify the number is even or odd"))

if(numberToIdentify % 2):
    print("Given number is odd")
else:
    print("Given number is even")

# ----------------------------------END-------------------------------------------------

# 3. Write a program which print the length of the list?
# ==================================START==============================================
numberList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 100, 14, 60, 50, 12, 19]

print("Length of the list is :", numberList.__len__())

# ----------------------------------END-------------------------------------------------

# 4. Write a Python program to sum all the numeric items in a list?
# ==================================START==============================================
_sum = 0
for number in numberList:
    _sum = number

print("Sum of list items is :", _sum)

# ----------------------------------END-------------------------------------------------

# 5. Write a Python program to get the largest number from a numeric list.
# ==================================START==============================================

_max = 0
for number in numberList:
    if(number > _max):
        _max = number
print("Max number is  :", _max)

# ----------------------------------END-------------------------------------------------

# 6. Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 100, 14, 60, 50, 12, 19]
# and write a program that prints out all the elements of the list that are
# less than 5.
# ==================================START==============================================

for number in numberList:
    if(number < 5):
        print("Less then 5:", number)
