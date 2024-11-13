RED = '\033[31m'
GREEN = '\033[1;32m'
BLUE = '\033[34m'
YELLOW = '\033[1;33m'
RESET = '\033[0m'

# 🏠 ДОМАШНЄ ЗАВДАННЯ


# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. 
print(f"{GREEN}Task 1{RESET}")
print(f"{BLUE}-" * 50 + RESET)
sentence = "Тіні спадали на землю, як пух із лелечого гнізда, лягали на річки, на гори, на хати, злегка ворушилися від вітерця. Між тими тінями стояв Іван, ніби заховавшися від людей, і чув, як його огортає чиста тиша вечора. Слухав, як дзвенить вода в потоці, як шепочуть трави, як поривається його душа кудись у висоту, до зір."
print(f'{YELLOW}Ось фрагмент оповідання Михайла Коцюбинського, "Тіні забутих предків":{RESET}')
print(sentence+"\n")

sentence = sentence.lower()
sentence = sentence.replace(',', '').replace('.', '')
words = sentence.split()
result = dict()

for word in words:
    result[word] = result.get(word, 0) + 1

print("Порахуємо кількість входжень слова в уривку: ")

for x,y in result.items():
    print(f"слово: {RED}{x}{RESET} кількість входжень: {RED}{y}{RESET}")

print(f"{BLUE}=" * 50 + "\n" + RESET)

# Task 2
# Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.
# The code has to return the dictionary with the sums of the prices by the goods types.

print(f"{GREEN}Task 2{RESET}")
print(f"{BLUE}-" * 50 + RESET)
total_prices = {}

for item in stock:
    total_prices[item] = stock[item] * prices[item]

print("Вартість запасів складає: ")

for x, y in total_prices.items():
    print(f"Товар: {RED}{x}{RESET} коштує: {RED}{y}{RESET} ")
print(f"{BLUE}=" * 50 + "\n" + RESET)


# Task 3

# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.

print(f"{GREEN}Task 3{RESET}")
print(f"{BLUE}-" * 50 + RESET)

task3 = [(x, x**x) for x in range(11)]
print(f"Результат виконання:\n{task3}")

print(f"{BLUE}=" * 50 + "\n" + RESET)

# Task 4

# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

print(f"{GREEN}Task 4{RESET}")
print(f"{BLUE}-" * 50 + RESET)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(f"Результат виконання:")
day_to_num = { i+1 : day for i, day in enumerate(days_of_week)}
num_to_day = { day : i+1 for i, day in enumerate(days_of_week)}

print(day_to_num)
print(num_to_day)
print(f"{BLUE}=" * 50 + "\n" + RESET)
