class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        
        for s in strs:

            freq = [0] * 26

            for char in s:

                freq[ord(char) - ord('a')] += 1

            hashmap[tuple(freq)].append(s)
        
        return list(hashmap.values())