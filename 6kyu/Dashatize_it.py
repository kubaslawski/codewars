"""
Given a variable n,

If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.

If n is not an integer, return the string "None".

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""

def dashatize(n):
    string = str(n)
    lst = []
    num = ""
    for char in string:
        if char.isdigit():
            if int(char) % 2 == 0:
                num += char
            else:
                if num:
                    lst.append(num)
                    num = ""
                lst.append(char)
    if num:
        lst.append(num)
    return '-'.join(lst) if len(lst) > 0 else 'None'
