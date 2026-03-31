class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Algorithm
        # Build a freq hashmap with nums. {1:1, 2:2, 3:3}
        # Build len(nums) + buckets and store each value in the freq buckets
        # Iterate these buckets from the end and keep adding to the output 
        # until len(output) == k and return.

        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
        
        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])
        
        for value, freq in freq_map.items():
            buckets[freq].append(value)
        
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
