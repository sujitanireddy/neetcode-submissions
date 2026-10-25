"""
          L
          R       
0 1 2 3 4 5
2,4,1,1,1,1
          
                                                1           2
                                            
                                        2   3   4   5

TC: O(n)
SC: O(n)


TC: O(n)
SC: O(1)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        L = 0
        R = 0
        max_range = 0
        res = 0
        
        while R < len(nums) - 1:

            for i in range(L, R+1):

                max_range = max(max_range, nums[i] + i)
            
            L += 1
            R = max_range
            res += 1
        
        return res