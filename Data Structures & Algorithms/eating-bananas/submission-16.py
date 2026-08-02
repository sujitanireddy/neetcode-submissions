class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """

        1  4  3  2          h = 9

           R
           L         
        1  2  3  4 

        - what is the min speed at which we can finish all the bananas
        
        What is the max? = max(piles) = O(n)

        1, 2, 3, 4

        go through each pile = 3//2  (pile/k) ceil of this value to decide how much time it's going to take
        """

        def valid_k(k):
            
            time = 0
            
            for pile in piles:
                time += math.ceil(pile/k)

            return time <= h

        L = 1
        R = max(piles)

        while L < R:

            mid = (L+R) // 2

            if valid_k(mid):
                R = mid
            
            else:
                L = mid + 1

        return R