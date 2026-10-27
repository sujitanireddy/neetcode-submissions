"""
[2,-1,1,2]

[2]

[2], [2,-1,1], [2], [-1,1,2]

prefix sums 

O(n) ** 2







"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        curr_sum = 0
        res = 0

        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            res += prefix_map[diff]
            prefix_map[curr_sum] += 1
        
        return res