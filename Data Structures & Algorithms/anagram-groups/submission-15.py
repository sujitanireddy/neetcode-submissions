class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_map = defaultdict(list)
        
        for word in strs:
            char_freq = [0] * 26
            for char in word:
                char_freq[ord(char) - ord('a')] += 1
            freq_map[tuple(char_freq)].append(word)
        
        return list(freq_map.values())
