"""
-1  0   1   0   1   0
0   1   2   3   4   5
0   1   1   0   1   0


Algo:
- if 0 then -1 else +1
- hashamp = 
{   
    0 : -1
    -1: 0
    1 : 1
}

- if a val is present in hashamp then calculate the dist = i - hahsmap[val]

Bruteforce:
TC: O(n**2)

Optimal:
O(n) 
O(n)
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        prefix_idx_map = defaultdict(int)
        prefix_idx_map[0] = -1
        res = 0
        curr_sum = 0

        for i, n in enumerate(nums):

            if n == 0:
                curr_sum -= 1
            else:
                curr_sum += 1
            
            if curr_sum in prefix_idx_map:
                res = max(res, i - prefix_idx_map[curr_sum])
            
            else:
                prefix_idx_map[curr_sum] = i
        
        return res

