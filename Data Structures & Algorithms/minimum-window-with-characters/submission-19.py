class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for c in t:
            t_freq[c] += 1
        
        need = len(t_freq)
        have = 0
        L = 0
        shortest_substring = ""

        for R in range(len(s)):

            s_freq[s[R]] += 1

            if s[R] in t_freq and t_freq[s[R]] == s_freq[s[R]]:
                have += 1
            
            while need == have:

                window = s[L:R+1]

                if not shortest_substring or len(window) < len(shortest_substring):
                    shortest_substring = window
                
                s_freq[s[L]] -= 1

                if s[L] in t_freq and s_freq[s[L]] < t_freq[s[L]]:
                    have -= 1

                L += 1
        
        return shortest_substring