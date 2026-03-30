class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #intution is we are trying to replace the other char with the max of char seen by far.

        L = 0
        alpha_freq = [0] * 26 #array to capture freq of letters seen in the string
        longest = 0

        for R in range(len(s)):

            alpha_freq[ord(s[R]) - 65] += 1

            while ((R - L) + 1) - max(alpha_freq) > k:

                alpha_freq[ord(s[L]) - 65] -= 1

                L += 1

            longest = max(longest, (R - L) + 1)
        
        return longest