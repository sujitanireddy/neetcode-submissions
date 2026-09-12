"""
s1 = "abc", s2 = "lecabee"   
{
    a : 1
    b : 1
    c : 1
}
      
s2 = []

a b c 

    L   
        R
0 1 2 3 4 5 6 7 8 9
l e c b b e e a b c

{
    a: 1
    b: 1 
    c: 1
    
}

TC : O(n)
SC : O(1)

edge case: if len(s1) > len(s2): return False
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        if s1_freq == s2_freq:
            return True
        
        L = 0
        for R in range(len(s1), len(s2)):
            s2_freq[ord(s2[R]) - ord('a')] += 1
            s2_freq[ord(s2[L]) - ord('a')] -= 1
            L += 1

            if s1_freq == s2_freq:
                return True

        return False


"""
s1="ab"

L   R
0 1 2 3 4 5 6
l e c a b e e

c = 1


"""
































