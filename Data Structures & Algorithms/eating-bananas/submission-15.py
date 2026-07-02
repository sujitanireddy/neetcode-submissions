class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def valid_k(k):

            time_taken = 0

            for pile in piles:

                time_taken += math.ceil(pile/k)
        
            return time_taken <= h
    
        
        L = 1
        R = max(piles)

        while L < R:

            mid = (L + R) // 2

            if valid_k(mid):
                R = mid

            else:
                L = mid + 1
        
        return R