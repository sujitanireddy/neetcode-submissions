class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_anagram_map = defaultdict(list)
    
        for s in strs:
            freq_arr = [0] * 26
            for c in s:
                freq_arr[ord(c) - ord('a')] += 1
            freq_anagram_map[tuple(freq_arr)].append(s)
        
        return list(freq_anagram_map.values())