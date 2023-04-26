"""
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
"""

def parse(data):
    lst = []
    num = 0
    for char in data:
        if char == "i":
            num += 1
        elif char == "d":
            num -= 1
        elif char == "s":
            num = num ** 2
        elif char == "o":
            lst.append(num)
    return lst
