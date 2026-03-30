class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        nums.sort()

        for i, a in enumerate(nums):

            if a > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums) - 1

            while l < r:

                if a + nums[l] + nums[r] == 0:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                elif a + nums[l] + nums[r] > 0:
                    r -= 1
                
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                

                
        return output

            
