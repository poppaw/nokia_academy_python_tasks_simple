# Create a function, which takes range and returns list of square roots of odd integers
# from given range (do not use loops)

# put your code here
import math


def count_square_roots(*arg):
    more_than_one_arg = len(arg) > 1
    start = arg[0] if more_than_one_arg else 0
    stop = arg[1] if more_than_one_arg else arg[0]
    roots_list = [math.sqrt(number) for number in range(start, stop) if number % 2 != 0]
    return roots_list


def count_square_roots_v2(*arg):
    more_than_one_arg = len(arg) > 1
    start = arg[0] if more_than_one_arg else 0
    stop = arg[1] if more_than_one_arg else arg[0]
    numbers = list(range(start, stop))
    odd_numbers = filter(lambda x: x % 2 != 0, numbers)
    roots_list = map(lambda y: math.sqrt(y), odd_numbers)
    return list(roots_list)


sq = count_square_roots(0, 100)
sq2 = count_square_roots_v2(0, 100)
assert sq == sq2
print(sq)
print(sq2)



