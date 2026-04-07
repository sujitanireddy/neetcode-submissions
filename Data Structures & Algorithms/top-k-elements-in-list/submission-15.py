class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #build freq_map for nums
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        #build empty buckets for freq
        n = len(nums)
        buckets = []
        for _ in range(n+1):
            buckets.append([])
        
        #map freq to buckets
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        #loop through and accumulate the output
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            
            for value in buckets[i]:

                output.append(value)

                if len(output) == k:

                    return output