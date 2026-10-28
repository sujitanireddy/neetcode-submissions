class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        L = max(nums)
        R = sum(nums)
        res = float("inf")

        def value_works(val):
            subarrays = 0
            counter = 0

            for n in nums:
                counter += n

                if counter > val:
                    subarrays += 1
                    counter = n

            return (1 + subarrays) <= k


        while L <= R:

            mid = (L+R) // 2

            if value_works(mid):
                res = min(res, mid)
                R = mid - 1
            
            else:
                L = mid + 1
        
        return res