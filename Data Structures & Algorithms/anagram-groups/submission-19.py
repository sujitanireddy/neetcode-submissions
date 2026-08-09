class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for word in strs:

            freq = [0] * 26

            for char in word:
                freq[ord(char)-ord('a')] += 1

            hashmap[tuple(freq)].append(word)
        
        return list(hashmap.values())
            


