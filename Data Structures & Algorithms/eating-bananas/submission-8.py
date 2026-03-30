class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def valid_k(mid):

            time_taken = 0

            for pile in piles:

                time_taken += math.ceil(pile/mid)

            return time_taken <= h

        
        L = 1
        R = max(piles)

        min_k_so_far = max(piles)

        while L <= R:

            mid = (L + R) // 2

            if valid_k(mid):

                min_k_so_far = min(min_k_so_far, mid)

                R = mid - 1
            
            else:

                L = mid + 1

        return min_k_so_far