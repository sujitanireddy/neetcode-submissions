class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        
        freq_map = defaultdict(list)

        for word in strs:

            freq_arr = [0] * 26

            for i in range(len(word)):
                freq_arr[ord(word[i]) - ord('a')] += 1
            
            freq_map[tuple(freq_arr)].append(word)
    
        return list(freq_map.values())