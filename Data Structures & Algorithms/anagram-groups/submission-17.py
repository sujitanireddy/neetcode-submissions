class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        { [0,0,0,0] : [] 

        }

        """

        hashmap = defaultdict(list) #[freq] : [strs]

        for s in strs:
            freq_map = [0] * 26
            for c in s:
                freq_map[ord(c) - ord('a')] += 1
            hashmap[tuple(freq_map)].append(s)
        
        return list(hashmap.values())
