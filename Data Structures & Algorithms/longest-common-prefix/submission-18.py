class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")
        longest_commin_prefix = ""
        for s in strs:
            min_length = min(min_length, len(s))
    
        for i in range(min_length):
            char = strs[0][i]
            
            for s in strs:
                if char != s[i]:
                    return longest_commin_prefix
            
            longest_commin_prefix += s[i]
        
        return longest_commin_prefix