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

     r2  r1  t
[2,  9,  8, 3]
  
 2   9  10   


rob1, rob2 = 0, 0

for i in range(len(nums)):

    temp = max(nums[i] + rob2, rob1)
    rob2 = rob1
    rob1 = temp

return rob1

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums1 = nums[:-1]
        nums2 = nums[1:]

        def dp(arr):

            rob1, rob2 = 0, 0

            for i in range(len(arr)):

                temp = max(arr[i] + rob2, rob1)
                rob2 = rob1
                rob1 = temp

            return rob1

        return max(dp(nums1), dp(nums2), nums[0])

            
       