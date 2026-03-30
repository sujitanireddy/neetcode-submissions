class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        print(freq_map)
        
        buckets = []
        for _ in range(len(nums)+1):
            buckets.append([])
        
        print(buckets)
        
        for value, freq in freq_map.items():
            buckets[freq].append(value)
        
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for value in buckets[i]:
                output.append(value)
            
            if len(output) == k:
                return output

