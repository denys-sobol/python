import random

# 🏠 ДОМАШНЄ ЗАВДАННЯ


# Task 1
# The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
# The result should be sent back to the user via a print statement.

num = random.randint(1,10)

def guess_number(num):
    while True:
        user_num = int(input("Вгадай число: "))
        if user_num == num:
            print(f"Вірно, ти виграв! Загадане число {num}")
            break
        else:
            command = input("Ні, спробувати ще? (1 - так / 2 - ні): ")
            if command == '2':
                print(f"Гра завершена, загадане число {num}. Дякуємо за участь!")
                break

guess_number(num)




# Task 2
# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”   

def birthday_greeting():
    name = input("Як Вас звуть? ") 
    age =  int(input("Скільки вам років? "))
    age += 1
    print(f"Привіт, {name}, на твій наступний день народження тобі виповниться {age} років")
 
birthday_greeting()

# Task 3
# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)

def string_distortion(string):
    for _ in range(5):
        result = random.choices(string, k=5)
        print(''.join(result))

string_distortion(input("Введіть рядок: "))