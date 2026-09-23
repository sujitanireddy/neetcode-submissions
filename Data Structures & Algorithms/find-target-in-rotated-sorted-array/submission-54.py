"""

        
        R 
0 1 2 3 4 5
3,4,5,6,1,2

if mid > R: L = Mid + 1
R = mid

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(L,R):

            while L <= R:

                mid = (L + R) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] > target:
                    R = mid - 1
                
                else:
                    L = mid + 1
            
            return None


        #find min 
        L = 0
        R = len(nums) - 1

        while L < R:

            mid = (L+R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            
            else:
                R = mid
        
        min_idx = R
        last_idx = len(nums) - 1

        if nums[min_idx] <= target <= nums[last_idx]:
            second_half = binary_search(min_idx, last_idx)
            if second_half != None:
                return second_half

        if nums[0] <= target <= nums[min_idx -1]:
            first_half = binary_search(0, min_idx - 1)
            if first_half != None:
                return first_half

        return -1