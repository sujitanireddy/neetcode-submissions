"""
[2 4 10 1 5]

2

1  | 0   2 |   3 |  5 

k = 4

minimun bound of my split is = max(nums)
max bound = sum(nums)

Binary serach 

Can we split this arrays into k subarrays so that the sum is 16? 

[2,4,10,1,5]

 2 6 16 1 6

    1 + 1 = 2 <= k


L                  M                R
10 11 12 13 14 15 16 17 18 19 20 21 22

22 + 10 // 2 = 

TC: log n
SC: O(1)

"""
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def valid_sum(val):
            
            subarrays = 0
            curr_sum = 0

            for n in nums:

                curr_sum += n

                if curr_sum > val:
                    subarrays += 1
                    curr_sum = n
            
            return subarrays + 1 <= k
       

        L = max(nums)
        R = sum(nums)
        res = float("inf")

        while L <= R:

            mid = (L+R) // 2

            if valid_sum(mid):
                res = min(res, mid)
                R = mid - 1
            
            else:
                L = mid + 1 
        
        return res







































