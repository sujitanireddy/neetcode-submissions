"""








"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        L = max(weights)
        R = sum(weights)
        res = float("inf")

        def capacity_works(cap):
            
            capacity = cap
            running_days = 1

            for w in weights:

                if capacity - w < 0:
                    capacity = cap
                    running_days += 1

                capacity -= w
            
            return running_days <= days


        while L <= R:

            mid = (L + R) // 2

            if capacity_works(mid):
                res = min(res, mid)
                R = mid - 1
            
            else:
                L = mid + 1
        
        return res
            