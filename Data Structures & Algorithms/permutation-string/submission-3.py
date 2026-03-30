class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_dict = defaultdict(int)
        for char in s1:
            s1_dict[char] += 1
        
        s2_dict = defaultdict(int)
        L = 0
        window_size = len(s1)
        
        for R in range(len(s2)):
            s2_dict[s2[R]] += 1

            if s1_dict == s2_dict:
                return True
            
            if window_size == (R - L) + 1:

                s2_dict[s2[L]] -= 1

                if s2_dict[s2[L]] == 0:
                    del s2_dict[s2[L]]
                
                L +=1
        
        return False


        
