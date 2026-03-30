class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        freq_array = [0] * 26
        L = 0

        for R in range(len(s)):

            freq_array[ord(s[R]) - ord('A')] += 1

            while ((R - L) + 1) - max(freq_array) > k:

                freq_array[ord(s[L]) - ord('A')] -= 1

                L += 1

            longest = max(longest, (R - L) + 1)

        return longest






     