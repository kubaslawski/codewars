"""
Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n < 2147483647

Examples
       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"
"""

def group_by_commas(n):
    strng = str(n)[::-1]
    res = ""
    for i in range(1 ,len(strng)):
        res += strng[i-1]
        if i % 3 == 0:
            res += ","
    res += strng[-1]
    return res[::-1]
    #your code here

x = group_by_commas(100000)
print(x)