class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
    
        #Build a dict with sorted word as key and an empty list
        for word in strs: 
            hashmap[''.join(sorted(word))] = []
        
        #For each word if it's sorted version is a key then append the word to a list
        for word in strs:
            sorted_word = ''.join(sorted(word))
            hashmap[sorted_word].append(word)

        return list(hashmap.values())

        

