class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1
        
        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])
        
        for value, freq in freq_dict.items():
            buckets[freq].append(value)

        output = []
        
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for value in buckets[i]:
                    output.append(value)

                    if len(output) == k:
                        return output


