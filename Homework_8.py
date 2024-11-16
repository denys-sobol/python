RED = '\033[31m'
GREEN = '\033[1;32m'
BLUE = '\033[34m'
YELLOW = '\033[1;33m'
RESET = '\033[0m'

# 🏠 ДОМАШНЄ ЗАВДАННЯ

# Task 1
# A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. The function should then print "My favorite movie is named {name}".
print(f"{GREEN}Task 1{RESET}")
print(f"{BLUE}-" * 50 + RESET)

def favorite_movie(movie):
    print(f'Мій улюблений фільм "{movie}"')
 
favorite_movie("Шоу Трумена")
print(f"{BLUE}=" * 50 + "\n" + RESET)

# Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the values of the dictionary to make sure that it works as intended.

print(f"{GREEN}Task 2{RESET}")
print(f"{BLUE}-" * 50 + RESET)

def make_country(country, capital):
    return {country : capital}

print(make_country("Україна","Київ"))
print(f"{BLUE}=" * 50 + "\n" + RESET)

# Task 3
# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

def make_operation(operator, *numbers):
    if not numbers:
        return "Введіть числа"
    elif len(numbers) == 1:
        return numbers[0]
    
    if operator == "+":
        return sum(numbers)
    elif operator == "-":
        num = numbers[0]
        for x in numbers[1:]:
            num -= x
        return num
    elif operator == "*":
        num = numbers[0]
        for x in numbers[1:]:
            num *= x
        return num
    else:
        return "Введіть один з операторів '+', '-', or '*'."

print(f"{GREEN}Task 3{RESET}")
print(f"{BLUE}-" * 50 + RESET)

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
print(f"{BLUE}=" * 50 + "\n" + RESET)

# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42  