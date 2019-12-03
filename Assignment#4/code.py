# Question1:
# Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary. Add a new key value pair about qualification then update the qualification value to high academic level then delete it.

# Question2:
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

# Question3:
# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

# Question4:
# Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

# Question5:
# Guess the number game
# Write a program which randomly generate a number between 1 to 30 and ask the user in input field to guess the correct number. Give three chances to user guess the number and also give hint to user if hidden number is greater or smaller than the number he given to input field.

# Question1:
from random import random
person = {
    "id": 1,
    "first_name": "John",
    "last_name": "Mike",
    "city": "France",
    "age": 24
}
for key in person.keys():
    print(key)
# Adding new key and value
person["qualification"] = "Graduate"

for key in person.keys():
    print(key)

# Updating qualification value
person["qualification"] = "Masters"

# deleting qualification
del person["qualification"]

for key in person.keys():
    print(key)

# Question2:
cities = {
    "karachi": {
        "country": "Pakistan",
        "population": "14.91 million",
        "fact": "Karachi is the largest and most populous metropolitan city in Pakistan and the capital of Sindh province."
    },
    "Lahore": {
        "country": "Pakistan",
        "population": "11.13 million",
        "fact": "Lahore is the capital of the Pakistani province of Punjab"
    },
    "Islamabad": {
        "country": "Pakistan",
        "population": "1.015 million",
        "fact": "Islamabad is the 9th largest city in Pakistan"
    }
}
# Print Keys in cities dictionary
for key in cities:
    print(key)
    for ky, val in cities[key].items():
        print(ky, "is", val)

# Print keys and values for every child
# for value in cities.values():
#     for key, val in value.items():
#         print(key, "is" , val)


# Question3:
while True:
    age = int(input("please enter age "))
    if(age > 0 and age < 3):
        print("the ticket is free")
    elif(age >= 3 and age <= 12):
        print("the ticket is $10")
    elif(age > 12):
        print("the ticket is $15")
    again = input("want ot check again , YES or NO ").lower()
    if(again != "yes"):
        break

# Question4:


def favorite_book(title="No title"):
    print("One of my favorite books is ", title)


favorite_book("Python")

# Question5:
chance = 0
while True:
    if(chance == 0):
        chance = 3
    if(chance == 3):
        randomNumber = int(random() * 30)
    userGuess = int(input("You have " + str(chance) +
                          " chance left to guess the number :"))
    if(userGuess == randomNumber):
        print("You Rock !")
        again = input("Do you want to play again ? YES or NO ").lower()
        if(again != "yes"):
            break
    else:
        chance -= 1
        if(chance == 0):
            print("You lose the number is ", randomNumber)
            again = input("Do you want to play again ? YES or NO ").lower()
            if(again != "yes"):
                break
