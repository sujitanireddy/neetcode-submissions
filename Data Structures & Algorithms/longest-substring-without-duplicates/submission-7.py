class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #Algorithm
        #Use a hashset to keep track of char's seen by far and move left and right pointers accordingly while keeping track of
        #the longest length of substring

        seen = set()
        L = 0
        length = 0

        for R in range(len(s)):

            while s[R] in seen:

                seen.remove(s[L])

                L += 1

            seen.add(s[R])

            length = max(length, R - L + 1)
        
        return length


        