class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(array):

            L = 0
            R = len(array) - 1

            while L <= R:

                mid = (L + R) // 2

                if array[mid] == target:
                    return mid

                elif array[mid] > target:
                    R -= 1
                
                else:
                    L += 1
            
        
        L = 0 
        R = len(nums) - 1


        while L < R:

            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L += 1
            
            else:
                R = mid
        
        left_sorted_array = binary_search(nums[:R])
        right_sorted_array = binary_search(nums[R:])

        if left_sorted_array != None:
            return left_sorted_array
        
        elif right_sorted_array != None:
            return len(nums[:R]) + right_sorted_array

        else:
            return -1 