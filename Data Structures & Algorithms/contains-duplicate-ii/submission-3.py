class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        sett = set()

        L = 0

        for R in range(len(nums)):

            if (R - L) + 1 > k + 1:

                sett.remove(nums[L])

                L += 1
            
            if nums[R] in sett:

                return True
            
            sett.add(nums[R])
        
        return False