"""

len >= 2
        i
23  25  29  25  42  

0   1   2   3   4
23  2   4   6   7


{
    0 : -1  #reminder : idx
    5 : 0
    1 : 1
}

2 - 0 > 1:
return True

r = 23 % 6 = 5 
r = 25 % 6 = 1
r = 29 % 6 = 5



"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        curr_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = -1
        res = 0

        for i, n in enumerate(nums):

            curr_sum += n
            remainder = curr_sum % k

            if remainder in prefix_map:
                if i - prefix_map[remainder] > 1:
                    return True
                
            else:
                prefix_map[remainder] = i
        
        return False