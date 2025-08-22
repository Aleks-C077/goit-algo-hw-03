# Функція №2

import random

def get_numbers_ticket(min, max, quantity):
    """
    Функція генерує вказану кількість унікальних чисел у заданому діапазоні і 
    повертає список випадково вибраних, відсортованих чисел. 
    """
    list_of_random_numbers = []

    if (max - min) < quantity:
        return list_of_random_numbers
    
    if not (1 <= min < max <= 1000): 
        return list_of_random_numbers

    if min >= 1 and max <= 1000:
        for i in range(min,max):

            list_of_random_numbers.append(random.randrange(min,max))
    result = random.sample(list_of_random_numbers,quantity)
    result.sort()

    return result


# print(get_numbers_ticket(-10,10,5))

# Функція № 2 варіант 2
import random

def get_numbers_ticket(min, max, quantity):
    """
    Генерує вказану кількість унікальних чисел у діапазоні [min, max]
    та повертає відсортований список.
    """
    if (max - min + 1) < quantity:
        return []
    
    if not (1 <= min < max <= 1000):
        return []

    result = random.sample(range(min, max + 1), quantity)
    return sorted(result)