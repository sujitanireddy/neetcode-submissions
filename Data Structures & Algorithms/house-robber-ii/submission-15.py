"""
[3,4,3]

 i         
[2,9,8,3,6]

 
[9,8,3,6]

f(i) = max(nums[i] + f(i+2), f(i+1))

[2,9,8,3]

Top down memoization:
O(n)
O(n)

True Dp Sol:
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums1 = nums[:-1]
        nums2 = nums[1:]

        cache = {}

        def recurse(i, arr, arr_no):

            if (i,arr_no) in cache:
                return cache[(i,arr_no)]
            
            if i >= len(arr):
                return 0
            
            cache[(i,arr_no)] = max(arr[i] + recurse(i+2, arr, arr_no), recurse(i+1, arr, arr_no))

            return cache[(i,arr_no)]
        
        return max(recurse(0, nums1, 1), recurse(0, nums2, 2), nums[0])