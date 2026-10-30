class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
    
        s_char_freq = [0] * 26 #array of 26 0's
        t_char_freq = [0] * 26
        
        for i in range(len(s)):
            s_char_freq[ord(s[i]) - ord('a')] += 1
            t_char_freq[ord(t[i]) - ord('a')] += 1
        
        return s_char_freq == t_char_freq