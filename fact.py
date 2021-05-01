def factorial(n: int) -> int:
    """
    Function to calculate the factorial
    :param n: The number whose factorial is to be calculated
    :return: The factorial value
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


for i in range(0, 36):
    print("{0}  {1}".format(i, factorial(i)))
