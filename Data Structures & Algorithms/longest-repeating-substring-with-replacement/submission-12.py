class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
        
                  R
              L
        A A A B A B B


            A B
        max(1 2) + 1  < window

        """
        L = 0
        freq = [0] * 26
        longest = 0

        for R in range(len(s)):

            freq[ord(s[R]) - ord('A')] += 1

            while (max(freq) + k) < ((R - L) + 1):
                freq[ord(s[L]) - ord('A')] -= 1
                L += 1
            
            longest = max(longest, (R - L + 1))
            
        
        return longest