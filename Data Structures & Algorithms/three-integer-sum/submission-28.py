class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []

        for i, a in enumerate(nums):

            if a > 0:
                break
            
            if i > 0 and nums[i-1] == a:
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:

                if nums[L] + nums[R] + a == 0:

                    output.append([nums[L], nums[R], a])

                    L += 1
                    R -= 1

                    while L < R and nums[L-1] == nums[L]:
                        L += 1
                    
                    while L < R and nums[R + 1] == nums[R]:
                        R -= 1
                        
                elif nums[L] + nums[R] + a > 0:
                    R -= 1
                
                else:
                    L += 1
        
        return output