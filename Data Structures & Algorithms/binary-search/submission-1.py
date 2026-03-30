class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start_index = 0
        end_index = len(nums) - 1
        

        while start_index <= end_index:
            
            median_index = (start_index + end_index) // 2

            if nums[median_index] == target:
                return median_index
            
            elif nums[median_index] > target:

                end_index = median_index - 1
            
            else:
                start_index = median_index + 1
        
        return -1