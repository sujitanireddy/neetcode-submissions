"""

4   9   9    7     4    5  

4   5   0   -2    -3    1


k = 5

{
    curr_sum % k = count

}

0 : 2
1 : 1
9 %

"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        res = 0

        for n in nums:
            curr_sum += n
            remainder = curr_sum % k

            res += prefix_map[remainder]
            prefix_map[remainder] += 1
        
        return res
