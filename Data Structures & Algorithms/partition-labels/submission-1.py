"""
i
_
x y x x y  z b z b b    i   s   l

{
    x : 3
    y : 2
    z : 2
    b : 1
    i : 1
    s : 1
    l : 1
}

set()
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        res = []
        
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1

        sett = set()

        L = 0
        for R in range(len(s)):

            if s[R] not in sett:
                sett.add(s[R])
            
            freq_map[s[R]] -= 1

            if freq_map[s[R]] == 0:
                sett.remove(s[R])
                
                if not sett:
                    res.append((R - L) + 1)
                    L = R + 1
        
        return res
            
            

        
