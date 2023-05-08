"""
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
"""

def sum_strings(x, y):
    num_x = [int(char) for char in x[::-1]]
    num_y = [int(char) for char in y[::-1]]

    length = max(len(num_x), len(num_y))
    num_x += [0] * (length - len(num_x))
    num_y += [0] * (length - len(num_y))

    res = []
    prev_modulo = 0
    for i in range(length):
        digit_sum = num_x[i] + num_y[i] + prev_modulo
        prev_modulo = digit_sum // 10
        res.append(digit_sum % 10)
    if prev_modulo:
        res.append(prev_modulo)
    final_num = ''.join([str(num) for num in res[::-1]]).lstrip("0")
    return final_num if len(final_num) > 0 else "0"