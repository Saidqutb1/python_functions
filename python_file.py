# counter = 1
# while counter <= 5:
#     print(f'Counter is: {counter}')
#     counter += 1
# from typing import List

# my_list = [0, 1, 2]
# while my_list:
#     element = my_list.pop()
#     print(f"element: {element}")

# print(my_list)


# while True:
#     print('Infinite loap!')

# while True:
#     answer = input('Enter a number: ')
#     if answer == 'quit':
#         break
#     print(f'You entered {answer}')


# Coin game
# import random

# HEADS = 'heads'
# TAILS = 'tails'
# COIN_VALUES = [HEADS, TAILS]

# def flip_coins():
#     return random.choice(COIN_VALUES)

# print(flip_coins())


# for i in range(1, 11):
#     for j in range(1, 11):
#     print()


# import json
#
# informations = {
#     'name': 'Saidqutb',
#     'age': '21',
#     'city': 'Andijan',
#     'school': 'nomer 5'
# }
#
#
# json_format = json.dumps(informations)
# print(json_format)

# s = []
# f = []
# a = [23, 32, 32, 32, 32, 33, 37, 32]
# for i in a:
#     if i % 2 == 0:
#         s.append(i)
#     else:
#         f.append(i)
# print(f)
# print(s)


from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(a):
    if a < 2:
        return a
    return fibonacci(a - 1) + fibonacci(a - 2)


a = int(input("--->"))
print(fibonacci(a))




