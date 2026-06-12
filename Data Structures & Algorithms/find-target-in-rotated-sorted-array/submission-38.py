class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(L, R):
            while L <= R:
                mid = (L + R) // 2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    L = mid + 1
                else:
                    R = mid - 1
            return -1
        
        L = 0
        R = len(nums) - 1
        while L < R:
            mid = (L + R) // 2
            if nums[R] < nums[mid]:
                L = mid + 1
            else:
                R = mid

        min_index = R
        last_index = len(nums) - 1

        if nums[0] <= target <= nums[-1]:
            return binary_search(0, last_index)
        
        elif nums[0] <= target <= nums[min_index - 1]:
            return binary_search(0, min_index)
        
        else:
            return binary_search(min_index, last_index)