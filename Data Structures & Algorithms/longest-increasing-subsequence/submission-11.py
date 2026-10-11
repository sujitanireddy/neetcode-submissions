"""
       i
[9,1,4,2,3,3,7]
LIS = 1

                                      [9]                               []

                            X[9,1]          [9]                 [1]             []

                                                [9]     [1,4]       [1]       [4]   []  

                                                        [1,4,7]           [1,2]

                                                                            [1,2,3]

                                                                                [1,2,3,7]
Brute Force Recursive way:
- O(2**n)
- O(n)

Top down memoization:
- O(n)
- O(n)

def recurse(i, prev):

- Base Cases:

    if i >= len(nums):
        return 0

    Choose:
    if prev < nums[i]:
        1 + recurse(i+1, nums[i])
    
    Skip:
    recurse(i+1, prev)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = {}

        def recurse(i,prev):

            if (i,prev) in cache:
                return cache[(i,prev)]
            
            if i >= len(nums):
                return 0

            skip, choose = 0, 0
            
            #skip
            skip = recurse(i+1, prev)

            #choose
            if prev < nums[i]:
                choose = 1 + recurse(i+1, nums[i])

            cache[(i,prev)] = max(skip,choose)

            return max(skip, choose)

        return recurse(0,float("-inf"))







































        