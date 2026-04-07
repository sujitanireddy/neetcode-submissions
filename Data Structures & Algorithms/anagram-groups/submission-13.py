class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)
        
        for word in strs:
            freq_arr = [0] * 26
            for char in word:
                freq_arr[ord(char) - ord('a')] += 1
            anagram_map[tuple(freq_arr)].append(word)
        
        return list(anagram_map.values())