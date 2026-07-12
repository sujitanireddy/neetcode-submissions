class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        [3,4,5,6    1,2]

                  
            L   R
        0 1 2 3 4 5
        3,5,6,0,1,2
        
        Binary Search
        while L < R
        - Is nums[R] < nums[mid]? -> Our search should shift to the left
        - R = M

        - Find the partition point where the array is broken down into two sorted arrays

        TC: O(log n)
        SCL O(1)

        """
        def binary_search(l,r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1 

        #[3,5,6,0,1,2]
        L = 0 
        R = len(nums) - 1

        while L < R:
            mid = (L+R)//2
            if nums[R] < nums[mid]:
                L = mid + 1
            else:
                R = mid
        
        patition_point = L
        
        if nums[0] <= target <= nums[-1]:
            l = 0
            r = len(nums) - 1
            return binary_search(l,r)

        elif nums[0] <= target <= nums[patition_point - 1]:
            l = 0
            r = patition_point - 1
            return binary_search(l,r)
        
        elif nums[patition_point] <= target <= nums[-1]:
            l = patition_point
            r = len(nums) - 1
            return binary_search(l,r)

        else:
            return - 1
