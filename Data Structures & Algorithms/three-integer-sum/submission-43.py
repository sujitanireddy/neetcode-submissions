"""
            L R
1       3 3 4 5 2 2



"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            triplets = []
            nums.sort()
    
            for i, a in enumerate(nums):
                if a > 0:
                    break
                if i > 0 and a == nums[i - 1]:
                    continue
                
                L = i + 1
                R = len(nums) - 1
                
                while L < R:
                    
                    summ = a + nums[L] + nums[R]

                    if summ == 0:

                        triplets.append([a,nums[L],nums[R]])

                        L += 1
                        R -= 1
                        
                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
                        
                        while L < R and nums[R] == nums[R + 1]:
                            R -= 1
                        
                    
                    elif summ > 0:
                        R -= 1
                    
                    else:
                        L += 1
            
            return triplets