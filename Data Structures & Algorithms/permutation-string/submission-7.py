class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #algorithm
        #keep a freq array for s1. 
        #Traverse R through the entire s2 and if the window limit is hit then move L pointer and add R pointer.
        #If the condition is met where freq array of s1 and s2 match then return true else false

        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for i in range(m):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        if s1_freq == s2_freq:
            return True
        
        for i in range(m, n):
            s2_freq[ord(s2[i]) - ord('a')] += 1
            s2_freq[ord(s2[i - m]) - ord('a')] -= 1

            if s1_freq == s2_freq:
                return True
        
        return False
        