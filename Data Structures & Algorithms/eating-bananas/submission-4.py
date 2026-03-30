class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def K_works(mid):
            
            time_taken = 0
            
            for pile in piles:

                time_taken += math.ceil(pile/mid)
            
            return time_taken <= h


        L = 1 
        R = max(piles)

        while L < R:

            mid = (L + R) // 2

            if K_works(mid):
                R = mid
            
            else:
                L = mid + 1
        
        return L


       