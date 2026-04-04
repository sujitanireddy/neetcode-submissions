class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1
        
        need = len(t_dict)
        have = 0
        L = 0
        best_window = ""

        s_dict = defaultdict(int)

        for R in range(len(s)):

            s_dict[s[R]] += 1

            if s[R] in t_dict and s_dict[s[R]] == t_dict[s[R]]:
                have += 1
            
            while need == have:

                window = s[L:R+1]

                if not best_window or len(window) < len(best_window):

                    best_window = window
                
                s_dict[s[L]] -= 1
                
                if s[L] in t_dict and s_dict[s[L]] < t_dict[s[L]]:

                    have -= 1
                
                L += 1
        
        return best_window

