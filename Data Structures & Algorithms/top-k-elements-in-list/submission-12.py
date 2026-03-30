class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        print(freq_map)
        
        buckets = []
        for _ in range(len(nums) + 1): #if we take 1 freq of each number the max freq buckets we would need are len(nums) + 1
            buckets.append([])
        
        print(buckets)

        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            
            for num in buckets[i]:

                output.append(num)

            if len(output) == k:

                return output
        