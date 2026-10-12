"""
            i
c   a   t

                    j
c   r   a   b   t

1
1
1

+1 when matching

if i == len(text1) or j == len(tex2):
    return 0

Conditions:
- If text1[i] == text2[j]:
    recurse(i+1,j+1)
- else:
    - recurse(i, j+1)
    - recurse(i+1,j)

Brute Force recursion:
TC: O(2**n)
SC: O(m*n)

Top down memo:
TC: O(m*n)
SC: O(m*n)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}
        
        def recurse(i,j):

            if (i,j) in cache:
                return cache[(i,j)]

            if i >= len(text1) or j >= len(text2):
                return 0
            
            if text1[i] == text2[j]:
                res = 1 + recurse(i+1, j+1)
            
            else:
                res = max(recurse(i+1, j), recurse(i, j+1))

            cache[(i,j)] = res

            return res

        return recurse(0,0)