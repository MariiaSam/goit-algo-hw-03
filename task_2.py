import random


def get_numbers_ticket(min, max, quantity):
    if 1 <= min <= max <= 1000 and quantity <= (max - min):
        random_numbers = random.sample(range(min, max), quantity)
        random_numbers.sort()
        return random_numbers
    return []


lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Ваші лотерейні числа:", lottery_numbers)
