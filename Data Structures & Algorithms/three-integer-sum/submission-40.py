class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """

            a  
        -4 -1 -1 0 1 2

        [[-1,-1,2], [-1 0 1]
        """

        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i-1]:
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:

                summ = a + nums[L] + nums[R]

                if summ == 0:
                    
                    res.append([a, nums[L], nums[R]])

                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1

                elif summ > 0:
                    R -= 1
                
                else:
                    L += 1

        return res