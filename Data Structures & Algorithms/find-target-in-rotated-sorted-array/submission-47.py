class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(L,R):

            if L > R:
                return -1

            mid = (L + R) // 2
            
            if target == nums[mid]:
                return mid

            elif nums[L] <= nums[mid]:
                if nums[L] <= target <= nums[mid]:
                    return binary_search(L,mid-1)
                else:
                    return binary_search(mid+1,R)
            
            elif nums[mid] <= target <= nums[R]:
                    return binary_search(mid+1, R)
            
            else:
                return binary_search(L, mid-1)
            
            return -1

        
        return binary_search(0,len(nums)-1)