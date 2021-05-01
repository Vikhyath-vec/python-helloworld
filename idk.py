def fizz_buzz(n: int) -> str:
    """
    This functions is used for the fizz_buzz game
    :param n: It is the number given by the user
    :return: Returns what is supposed to be said
    """

    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return "{}".format(n)


for i in range(1, 101):
    result = fizz_buzz(i)
    print(result)