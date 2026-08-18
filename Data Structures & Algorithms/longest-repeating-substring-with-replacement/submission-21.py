"""
L
      R
X Y Y X

        L
            R

0 1 2 3 4 5 6
A A B A B B A

4

       A B C D   X Y Z
arr = [4,1,0,0...0 0 0]

TC: O(n)
SC: O(1)
            

(window_length - max(arr)) <= 1 : allowed to move

6 - 4 <= 1


relative position in my arr: ord('s[i]') - ord('A')

replacements = 1

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        arr = [0] * 26
        L = 0
        window = 0

        for R in range(len(s)):

            arr[ord(s[R]) - ord('A')] += 1
            
            while ((R-L) + 1) - max(arr) > k:
                arr[ord(s[L]) - ord('A')] -= 1
                L+=1

            window = max(window, (R - L) + 1)
            
        return window


