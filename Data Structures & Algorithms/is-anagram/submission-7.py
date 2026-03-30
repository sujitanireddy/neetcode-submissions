class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}

        for letter in s:
            s_dict[letter] = 1 + s_dict.get(letter, 0)
        
        for letter in t:
            t_dict[letter] = 1 + t_dict.get(letter, 0)
        
        if s_dict == t_dict:
            return True
        
        else:
            return False