class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def k_valid(k):

            time_taken = 0

            for pile in piles:

                time_taken += math.ceil(pile/k)

                print(time_taken)

            return time_taken <= h
        
        
        L = 1
        R = max(piles)

        while L < R:

            mid = (L + R) // 2

            print(mid)

            if k_valid(mid) == True:
                R = mid
            
            else:
                L = mid + 1
        
        return R
            