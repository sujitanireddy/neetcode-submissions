class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        sorted_freq = sorted(freq_map.items(), key = lambda x: x[1], reverse= True)
        
        output = []
        for i in range(k):
            output.append(sorted_freq[i][0])
        
        return output
