class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #log time = binary search algorithm. I know how to find min in a rotated sorted array.
            # Find min in rotated sorted array 
            # adjust pointers according to given target
            # Regular binary search
        L = 0 
        R = len(nums) - 1

        while L < R: 
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1 
            
            else:
                R = mid
        
        minimum = L

        if nums[minimum] <= target <= nums[-1]:
            L = minimum
            R = len(nums) - 1

        elif nums[0] <= target <= nums[minimum - 1]:
            L = 0
            R = minimum - 1

        
        
        
        while L <= R:

            mid = (L + R) // 2

            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                L = mid + 1 
            
            else:
                R = mid - 1
        
        return -1 