"""
k = 1
L
          R
A A A B A B B

 A B C....Z
[2,2,0....0]

window len - max(arr) <= k
6-2
2 <= k
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        arr = [0] * 26
        L = 0

        for R in range(len(s)):

            arr[ord(s[R]) - ord('A')] += 1

            while ((R - L) + 1) - max(arr) > k:
                
                arr[ord(s[L]) - ord('A')] -= 1

                L += 1

            res = max(res, (R-L) + 1)
        
        return res