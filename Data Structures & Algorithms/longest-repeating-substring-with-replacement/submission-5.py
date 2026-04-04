class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        L = 0 
        freq_arr = [0] * 26

        for R in range(len(s)):

            freq_arr[ord(s[R]) - ord('A')] += 1

            while (R - L + 1) - max(freq_arr) > k:

                freq_arr[ord(s[L]) - ord('A')] -= 1

                L +=1

            longest = max(longest, R - L + 1)
        
        return longest

                
