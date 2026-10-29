"""
        L M  LR      
5,7,7,8,8,8,10
0 1 2 3 4 5 6

BruteForce: O(n), O(n)

Notes:
- if target is found don't stop, look for either leftbiased or rightbiased
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search_biased(leftbiased):
            L = 0
            R = len(nums) - 1
            i = -1

            while L <= R:

                mid = (L+R) // 2

                if target > nums[mid]:
                    L = mid + 1
                
                elif target < nums[mid]:
                    R = mid - 1
                
                else:
                    i = mid
                    if leftbiased:
                        R = mid - 1
                    else:
                        L = mid + 1
            
            return i

        left_val = binary_search_biased(True)
        right_val = binary_search_biased(False)

        return [left_val, right_val]