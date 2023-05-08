"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


def increment_string(strng):
    word = list(strng)
    reversed_num = []
    for i, x in enumerate(strng[::-1]):
        if x.isdigit():
            reversed_num.append(x)
            word.pop()
        else:
            break
    num = reversed_num[::-1]
    leading_zeros, rest = '', ''
    for i, x in enumerate(num):
        if x == '0':
            leading_zeros += x
        else:
            rest = ''.join(num[i:])
            break
    if rest == '':
        y = '1'
    else:
        y = str(int(rest) + 1)
    if len(y) > len(rest) or len(rest) == 0:
        leading_zeros = leading_zeros[:-1]
    return ''.join(word) + leading_zeros + y

# Time: 520s
