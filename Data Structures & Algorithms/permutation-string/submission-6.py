class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #algorithm
        #if s1 > s2: substring cannot exist: return False
        #Build a freq_map of s1. Check if it matches freq_map of s2 and keep sliding the window. If matches then return true

        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        s1_freq_arr = [0] * 26
        s2_freq_arr = [0] * 26
        for i in range(m):
            s1_freq_arr[ord(s1[i]) - ord('a')] += 1
            s2_freq_arr[ord(s2[i]) - ord('a')] += 1
        
        if s1_freq_arr == s2_freq_arr:
            return True
        
        #till m we already validated
        for i in range(m, n):
            s2_freq_arr[ord(s2[i]) - ord('a')] += 1
            s2_freq_arr[ord(s2[i - m]) - ord('a')] -= 1

            if s1_freq_arr == s2_freq_arr:
                return True
        
        return False

        
        
        

        