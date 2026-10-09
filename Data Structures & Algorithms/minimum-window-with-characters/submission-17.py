class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_freq = defaultdict(int)
        s_freq = defaultdict(int)
        
        for char in t:
            t_freq[char] += 1
        
        need = len(t_freq)
        have = 0
        L = 0
        res = ""

        for R in range(len(s)):

            s_freq[s[R]] += 1

            if s[R] in t_freq and t_freq[s[R]] == s_freq[s[R]]:
                have += 1
            
            while need == have:

                window = s[L:R+1]

                if not res or len(window) < len(res):
                    res = window
                
                s_freq[s[L]] -= 1
                
                if s[L] in t_freq and s_freq[s[L]] < t_freq[s[L]]:
                    have -= 1

                L += 1 

        return res