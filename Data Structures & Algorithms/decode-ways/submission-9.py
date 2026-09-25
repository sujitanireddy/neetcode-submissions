""" 
1   0   1   2
  J     A   B
  J     L

1   2
A   B
 L

0   1
X

0   1   2   3
        i       
1   1   2   3       

s[2:3]

Observation:
- if we reach the end then that's a valid way
- if you encounter a single zero you are stuck
- Just two digit check is the max with the range being from 1 - 26

Brute force Recurive way:

Base case: 
    if len(s) == i:
        return 1

    res = recurse(i+1)

    if i < len(s) - 1 and 1 <= int(s[i:i+1]) <= 26:
        res += recurse(i+2)
    
    return res

recurse(0)

TC analysis

O(n)

TC: O(2**n)
SC: O(n)

Top down memoization



"""
class Solution:
    def numDecodings(self, s: str) -> int:

        res = [0]
        cache = {}

        def recurse(i):

            if i in cache:
                return cache[i] 

            if len(s) == i:
                return 1    #found a valid way

            if s[i] == "0":
                return 0
            
            #check single decode possible or not
            cache[i] = recurse(i+1)

            #check if double digit deocde is possible or not
            if i < len(s) - 1 and 1 <= int(s[i:i+2]) <= 26:
                cache[i] += recurse(i+2)
                #cache[i] += res[0]

            return cache[i]

        return recurse(0)






































        