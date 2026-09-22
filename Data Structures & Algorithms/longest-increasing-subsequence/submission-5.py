class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        cache = {}
    
        def recurse(i,j):
            
            if (i,j) in cache:
                return cache[(i,j)]

            #base case
            if i == n:
                return 0

            #skip
            res = recurse(i+1, j)

            #when can I choose?
            if j == -1 or nums[j] < nums[i]:
                res = max(1 + recurse(i+1, i), res)
                cache[(i,j)] = res
            
            return res
        
        
        return recurse(0,-1)