class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = defaultdict(int)
        output = []

        for num in nums:
            freq_map[num] += 1
        
        buckets = []
        for _ in range(len(nums)+1):
            buckets.append([]) 

        for key, value in freq_map.items():
            buckets[value].append(key)

        for i in range(len(buckets)- 1, -1 , -1):

            if not buckets[i]:
                continue
            
            for val in buckets[i]:
                output.append(val)
            
            if len(output) == k:
                break
        
        return output

    