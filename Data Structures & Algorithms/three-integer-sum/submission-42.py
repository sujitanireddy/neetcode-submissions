"""
[-1,0,1,2,-1,-4]

     i  L     R
[-4,-1,-1,0,1,2]

TC: O(n**2)
SC: O(n)


if we see a duplicate anchor then just skip it

if we see duplicates in two pointers, skip them

if we found a sol:
    move L and R pointers


[-1,-1,2]. [-1,0,1]

L < R
-4,-1,2 > or < 0? 

O(nlogn)
Brute Force: O(n**4)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        for i, a in enumerate(nums):

            if a > 0:
                break
            
            #skip duplicates in the anchor
            if i > 0 and a == nums[i-1]:
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:

                summ = a + nums[L] + nums[R]

                if summ == 0:

                    res.append([a,nums[L],nums[R]])

                    L += 1
                    R -= 1

                    #skipping duplicates in the two pointer approach
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1

                elif summ < 0:
                    L += 1
                
                else:
                    R -= 1

        return res











































