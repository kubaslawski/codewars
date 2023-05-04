"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1
"""

def next_bigger(n):
    digits = list(str(n))
    for i in range(len(digits) -2, -1, -1):
        if digits[i] < digits[i + 1]:
            for j in range(len(digits) - 1, i, -1):
                if digits[j] > digits[i]:
                    digits[i], digits[j] = digits[j], digits[i]
                    break
            digits[i + 1:] = sorted(digits[i+ 1:])
            return int(''.join(digits))
    return -1