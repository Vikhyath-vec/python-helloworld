def palin_sen(string):
    word = ""
    for char in string:
        if char.isalnum():
            word += char
    return word[::-1].casefold() == word.casefold()


input_str = input("Please enter any sentence: ")
if palin_sen(input_str):
    print("{} is a palindrome".format(input_str))
else:
    print("{} is not a palindrome".format(input_str))
