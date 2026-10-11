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
- O(n**2)
- O(n**2)

def recurse(i, prev):

- Base Cases:

    if i >= len(nums):
        return 0

    Choose:
    if prev < nums[i]:
        1 + recurse(i+1, nums[i])
    
    Skip:
    recurse(i+1, prev)

Bottom up Tabulation:

9,1,4,2,3,3,7
1 4 3 3 2 2 1 

 0 1 2 3 4 5 6
 9,1,4,2,3,3,7
[0,0,3,3,2,2,1]


"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)

        for i in range(len(nums) - 2, -1 ,-1):
            for j in range(i+1, len(nums)):

                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)




































        