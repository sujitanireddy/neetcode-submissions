class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        Algorithm:
        - Sort the input array
        - if offset value is >=0. Break out of the loop
        - if the offset and offset[-1] are equal then skip
        - Initate two pointers. L = i + 1, R = len(nums) - 1
        - while L < R:
            if offset + nums[L] + nums[R] == 0
                triplets.append([offset, nums[L], nums[R]])
                L += 1
                R -= 1

                while L < R and nums[L] == nums[L-1]:
                    L += 1
                
                while L < R and nums[R] == nums[R+1]
                    R -= 1
            
            move the pointers accordingly.
        """

        triplets = []
        nums.sort()

        for i, a in enumerate(nums):

            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue
            
            L = i + 1
            R = len(nums) - 1 

            while L < R:

                if a + nums[L] + nums[R] == 0:
                    triplets.append([a, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1
                
                elif a + nums[L] + nums[R] > 0:
                    R -= 1
                
                else:
                    L += 1
        
        return triplets