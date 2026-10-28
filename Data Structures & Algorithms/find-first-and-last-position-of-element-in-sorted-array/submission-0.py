class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(leftbiased):

            L = 0
            R = len(nums) - 1
            i = -1

            while L <= R:

                mid = (L+R) // 2
                
                if nums[mid] > target:
                    R = mid - 1
                
                elif nums[mid] < target:
                    L = mid + 1

                else:
                    i = mid
                    if leftbiased:
                        R = mid - 1
                    else:
                        L = mid + 1
                
            return i
        
        left_bound = binary_search(True)
        right_bound = binary_search(False)

        return [left_bound, right_bound]