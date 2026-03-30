class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for word in strs:

            sorted_word = ''.join(sorted(word))

            hashmap[sorted_word] = []

        for word in strs:

            sorted_word = ''.join(sorted(word))

            hashmap[sorted_word].append(word)
        
        
        return list(hashmap.values())
            

        

