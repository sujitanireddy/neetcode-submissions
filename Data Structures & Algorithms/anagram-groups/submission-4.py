class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for word in strs:
            hashmap[''.join(sorted(word))] = []
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
        
        return list(hashmap.values())