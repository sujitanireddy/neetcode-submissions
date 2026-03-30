class Solution:
    def search(self, nums: List[int], target: int) -> int:

        search_start_index = 0
        search_end_index = len(nums) - 1

        while search_start_index <= search_end_index: 

            median = (search_start_index + search_end_index) // 2

            if nums[median] == target:
                return median

            elif nums[median] > target:

                search_end_index = median - 1

            else:
                search_start_index = median + 1
            
        return -1 
            