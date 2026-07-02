class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for c in t:
            t_dict[c] += 1
        
        need = len(t_dict)
        have = 0
        min_window = ""
        L = 0

        for R in range(len(s)):
            s_dict[s[R]] += 1

            if s[R] in t_dict and s_dict[s[R]] == t_dict[s[R]]:
                have += 1
            
            while need == have:

                window = s[L:R+1]

                if not min_window or len(window) < len(min_window):
                    min_window = window

                s_dict[s[L]] -= 1

                if s[L] in t_dict and s_dict[s[L]] < t_dict[s[L]]:
                    have -= 1

                L += 1

        return min_window
