def sum_numbers(*args: int) -> int:
    """
    A function to calculate the sum of all numbers entered.
    :param args: the list of numbers to be added
    :return: returns the sum
    """
    sum = 0
    for value in args:
        sum += value
    return sum


a = sum_numbers(1, 2, 3, 4, 5)
print(a)


