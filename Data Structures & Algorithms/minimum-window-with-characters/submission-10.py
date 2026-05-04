class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #s = "OUZODYXAZV" = {O:1,U:1,Z:1,D:1,Y:1,X:1} 

        t_freq = defaultdict(int)
        s_freq = defaultdict(int)
        
        for char in t:
            t_freq[char] += 1
        
        need = len(t_freq)
        have = 0
        best_window = ""
        
        L = 0
        for R in range(len(s)):
            s_freq[s[R]] += 1

            if s[R] in t_freq and s_freq[s[R]] == t_freq[s[R]]:
                have += 1        

            while need == have:

                window = s[L:R+1]

                if not best_window or len(window) < len(best_window):
                    best_window = window 

                s_freq[s[L]] -= 1

                if s[L] in t_freq and s_freq[s[L]] < t_freq[s[L]]:
                    have -= 1
                
                L+=1
        
        return best_window






