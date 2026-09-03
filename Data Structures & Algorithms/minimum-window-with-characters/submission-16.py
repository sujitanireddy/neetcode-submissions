"""
s = "OUZODYXAZV", t = "XYZ"

- while exploring, check if char is in t_map and the freq also matched for have to increment
- while have == need: 
        Start shriking the left pointer and keep calculating the min substring 
- if R goes out of bounds, we are done.

edge case: if len(t) > len(s): return ""

           L
                 R
s =  O U Z O D Y X A Z V  

s_map

have = 2

{
 O : 1
 U : 0
 Z : 0
 D : 0
 Y : 0
 X : 1
 A : 1
 Z : 1
 V : 1

 
}

t =  X Y Z
t_map

{
 X : 1
 Y : 1
 Z : 1
}
need = 3

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): return ""
        
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        
        L = 0
        need = len(t_map)
        have = 0
        min_window = ""
        
        for R in range(len(s)):

            s_map[s[R]] += 1

            if s[R] in t_map and s_map[s[R]] == t_map[s[R]]:
                have += 1

            while have == need:

                window = s[L:R+1]

                if not min_window or len(window) < len(min_window):
                    min_window = window
                
                s_map[s[L]] -= 1
                
                if s[L] in t_map and s_map[s[L]] < t_map[s[L]]:
                    have -= 1
                
                L += 1
        
        return min_window
            















































        