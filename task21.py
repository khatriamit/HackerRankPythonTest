"""
Welcome. In this kata, you are asked to square every digit of a number and 
concatenate them. For example, if we run 9119 through the function, 811181 will 
come out, because 92 is 81 and 12 is 1. Note: The function accepts an integer and 
returns an integer python
"""

# simple method
def square_digits(num):
    r = ""
    for l in str(num):
        r = r + str((int(l)) ** 2)
    return int(r)


a = square_digits(91119)
print(a)


# single line solution
def square_digits_opt(num):
    return int("".join(str(int(l) ** 2) for l in str(num)))


a = square_digits_opt(91119)
print(a)
