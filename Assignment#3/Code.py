

# 1. Make a calculator using Python with addition , subtraction , multiplication , division and power.
# ==================================START==============================================

firstNumber = int(input("Please enter your first integer value : "))
operator = input(
    "Please choose the operator from one of these, +, - , * , /, ^: ")
secondNumber = int(input("Please enter your second interger value : "))

if operator == '+':
    result = firstNumber + secondNumber
elif operator == '-':
    result = firstNumber - secondNumber
elif operator == '*':
    result = firstNumber * secondNumber
elif operator == '/':
    result = firstNumber / secondNumber
elif operator == '^':
    result = firstNumber ** secondNumber
else:
    result = "Invalid operator, Please choose the operator from one of these, +, - , * , /, ^:"

print(str(firstNumber)+str(operator)+str(secondNumber) +
      " = ", result, "Using if Condition")

# ===================================================
# Calculator using switch case
# ===================================================


def calculator(operator):
    switcher = {
        "+": firstNumber + secondNumber,
        "-": firstNumber - secondNumber,
        "*": firstNumber * secondNumber,
        "/": firstNumber / secondNumber,
        "^": firstNumber ** secondNumber,

    }
    return switcher.get(operator, "Invalid operator, Please choose the operator from one of these, +, - , * , /, ^ ")


print(f'{firstNumber} {operator} {secondNumber} = {result} Using switch case')

# ----------------------------------END-------------------------------------------------


# 2. Write a program to check if there is any numeric value in list using for loop
# ==================================START==============================================

valueList = [2, "test", 6.9, 12, True, 0, 19.5, [1, "abc"], '100']
for value in valueList:
    if(type(value) is int or type(value) is float):
        print("Numeric value in a list ", value)

# ----------------------------------END-------------------------------------------------

# 3. Write a Python script to add a key to a dictionary
# ==================================START==============================================

studentRecord = {
    'id': 1,
    'name': 'John',
    'age': 20,
    'displane': 'BSSE'
}
studentRecord["semister"] = "5th"
print(studentRecord)

# ----------------------------------END-------------------------------------------------

# 4. Write a Python program to sum all the numeric items in a dictionary
# ==================================START==============================================

_sum = 0
dictionary = {0: 2, 1: "data", 2: 6, 3: 12, 4: "python", 5: 8.9, 6: 0.1}
for value in dictionary.values():
    if(type(value) is int or type(value) is float):
        _sum += value
print(_sum)

# ----------------------------------END-------------------------------------------------

# 5. Write a program to identify duplicate values from list
# ==================================START==============================================

listAll = []
duplicate = []
listItem = [1, 2, "a", 3, 1, 4, "d",  3, 5,
            "b", 4, 6, "a",  2, 8, 9, 8, "b", 9, 6, "d"]
for number in listItem:
    if(number not in listAll):
        listAll.append(number)
    elif(number not in duplicate):
        duplicate.append(number)

for number in duplicate:
    print("Duplicate value ", number)

# ----------------------------------END-------------------------------------------------

# 6. Write a Python script to check if a given key already exists in a dictionary
# ==================================START==============================================

userRecord = {
    'name': 'John',
    'age': 21,
    'address': '123 Fake Street',
    'contact': '+012-458-657'
}

userKey = input("Please inter a key to get value: ")

if(userKey not in userRecord):
    print('No match found')
else:
    print(userRecord[userKey])

# ----------------------------------END-------------------------------------------------
