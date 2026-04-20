class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_map = defaultdict(list)

        for word in strs:
            
            freq = [0] * 26

            for char in word:

                freq[ord(char) - ord('a')] += 1

            freq_map[tuple(freq)].append(word)
        
        return list(freq_map.values())


