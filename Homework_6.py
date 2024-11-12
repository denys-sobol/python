import random

# 🏠 ДОМАШНЄ ЗАВДАННЯ


# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

index = 0
largest_num = 0

def random_num():
    numbers = []
    count = 0
    while count < 10:
        numbers.append(random.randint(1,10))
        count += 1
    return numbers

numbers = random_num()

while index < len(numbers):
    if largest_num < numbers[index]:
        largest_num = numbers[index]
    index += 1


print("\033[1;32mTask 1\033[0m")
print("\033[34m-\033[0m"*50)
print(f"Ряд згенерованих чисел: {numbers}")
print(f"Найбільше число в ряду: {largest_num}")
print("\033[34m=\033[0m"*50+"\n")


# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

numbers_1 = random_num()
numbers_2 = random_num()
common_elements = []
index = 0
 
while index < len(numbers_1):
    if numbers_1[index] in numbers_2 and numbers_1[index] not in common_elements:
        common_elements.append(numbers_1[index])
    index += 1

print("\033[1;32mTask 2\033[0m")
print("\033[34m-\033[0m"*50)
print(f"Спільні елементи для списків\nnumbers_1: {numbers_1}\nnumbers_2: {numbers_2}\n{common_elements}")
print("\033[34m=\033[0m"*50+"\n")

# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

count = 1
index = 0

integers_num = []
special_num = []

while count <= 100:
    integers_num.append(count)
    count+=1


while index != 99:
    if integers_num[index] % 7 == 0 and integers_num[index] % 5 != 0:
        special_num.append(integers_num[index])

    index += 1



print("\033[1;32mTask 3\033[0m")
print("\033[34m-\033[0m"*50)
print(f"Всі цілі числа, які діляться на 7, але не кратні 5 в діапазоні від 1 до 100:\n{special_num}")
print("\033[34m=\033[0m"*50+"\n")
