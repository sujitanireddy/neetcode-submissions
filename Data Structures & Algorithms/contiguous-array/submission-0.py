"""


0   1   2   2   3   3
0   1   1   0   1   0


{
    0: 1
    1: 1
    2: 2
    3: 2
}

0 : 2
1 : 1

    L
        R
0   0   1

0: 1
1: 1    

BruteForce: 
TC: O(n**2)
SC: O(1)

"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        prefix_map = defaultdict(int) #curr_sum : i (only map the earliest ones, so skip if seen later)
        prefix_map[0] = -1
        curr_sum = 0
        res = 0
        
        for i, n in enumerate(nums):

            if n == 1:
                curr_sum += 1
            else:
                curr_sum -= 1
            
            if curr_sum in prefix_map:
                res = max(res, i - prefix_map[curr_sum])
            
            else:
                prefix_map[curr_sum] = i
        
        return res


