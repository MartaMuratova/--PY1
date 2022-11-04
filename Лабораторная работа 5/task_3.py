import random


def get_unique_list_numbers() -> list[int]:
    b = range(-10, 10)
    ppp = random.sample(b, 15)
    return ppp


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
