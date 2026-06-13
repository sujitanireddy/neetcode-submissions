class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #sort the input array
        #use anchor and solve two sub problem
        #skip duplicates in anchor and two sub problem

        nums.sort()
        triplets = []

        for i, a in enumerate(nums):

            if i > 0 and nums[i-1] == a: #skipping duplicates in anchor
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:

                if nums[L] + nums[R] + a == 0:
                    triplets.append([a, nums[L], nums[R]])

                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    
                    while L < R and nums[R] == nums[R+1]:
                        R-=1
                
                elif nums[L] + nums[R] + a > 0:
                    R -= 1
                
                else:
                    L += 1

        
        return triplets