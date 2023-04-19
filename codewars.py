#определить, является ли это число квадратным числом:
import math


def is_square(n):
    return n >= 0 and math.sqrt(n) % 1 == 0 

def is_square(n):   
    return n > -1 and (n ** 0.5).is_integer()