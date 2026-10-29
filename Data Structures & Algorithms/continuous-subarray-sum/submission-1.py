"""
Notes:
- len > 1
- sum of subarray is multiple of k
- 0 is always a multiple
 
 23 25  29
[23, 2, 4,6,7]  k = 6
 0.  1. 2 3 4

BruteForce: O(n**2)

PrefixSums + hashmap: O(n), O(n)

{
    0 : -1
    5 : 0
    1 : 1
}


23 % 6 = 5
25 % 6 = 1
29 % 6 = 5

if my reminder is found: 
    i - value stored in hashmap > 1:
    return True
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        reminder_idx_map = defaultdict(int)
        reminder_idx_map[0] = -1
        curr_sum = 0
        res = 0

        for i, n in enumerate(nums):

            curr_sum += n
            rem = curr_sum % k

            if rem in reminder_idx_map:
                if i - reminder_idx_map[rem] > 1:
                    return True
            else:
                reminder_idx_map[rem] = i
        
        return False
