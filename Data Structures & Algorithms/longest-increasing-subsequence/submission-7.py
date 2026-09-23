"""
j  i
  [9,1,4,2,3,3,7]

                                    9   []
                                
                                9,1X

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = {}
        
        def recurse(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if len(nums) == i:
                return 0

            #include 
            res = recurse(i+1, j)

            #don't include
            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + recurse(i+1, i))
                cache[(i,j)] = res
            
            return res

        return recurse(0,-1)