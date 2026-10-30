class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)    #curr_sum -> freq
        freq_map[0] = 1
        curr_sum = 0
        subarrays = 0
        
        for n in nums:
            curr_sum += n
            if (curr_sum - k) in freq_map:
                subarrays += freq_map[curr_sum - k]
            freq_map[curr_sum] += 1
        
        return subarrays
        