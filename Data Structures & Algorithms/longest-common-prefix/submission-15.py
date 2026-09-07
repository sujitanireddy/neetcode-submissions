class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
	
	
        for i in range(n):
            for word in strs:
                if len(word) == i or strs[0][i] != word[i]:
                    return word[:i]
        
        return strs[0]
