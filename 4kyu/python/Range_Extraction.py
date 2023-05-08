"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
Courtesy of rosettacode.org
"""


def solution(args):
    ranges = []
    num_1 = args[0]
    num_2 = args[0]
    for i in range(1, len(args)):
        if args[i] - args[i - 1] == 1:
            num_2 = args[i]
        else:
            if num_1 == num_2:
                ranges.append(str(num_1))
            else:
                ranges.append(f"{num_1}-{num_2}")
            num_1 = args[i]
            num_2 = args[i]
    if num_1 == num_2:
        ranges.append(str(num_1))
    else:
        ranges.append(f"{num_1}-{num_2}")
    strng = ",".join(ranges)
    return strng

x = solution([1, 2, 4, 5, 6, 7, 9, 10])
print(x)
