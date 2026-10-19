"""
- the max is always splitting into one char.
- build a freq map using a hashmap
- while traversing the array, keep decrementing until it's 0 while also keeping track of all the chars.


hashset and hashmap
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []

        freq_map = {}
        for char in s:
            freq_map[char] = 1 + freq_map.get(char, 0)
        
        sett = set()

        L = 0

        for R in range(len(s)):

            sett.add(s[R])
            freq_map[s[R]] -= 1

            if freq_map[s[R]] == 0:
                sett.remove(s[R])
            
            if not sett:
                size = len(s[L:R+1])
                res.append(size)
                L = R + 1

        return res