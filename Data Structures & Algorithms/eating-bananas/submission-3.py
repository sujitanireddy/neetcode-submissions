class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def time_taken(mid):

            time_taken = 0
            
            for pile in piles:
                time_taken += math.ceil(pile/mid)
            
            return time_taken

        #we know the range: 1 to max_speed. As we know the range we can apply binary search here.
        right = max(piles)
        left = 1

        while left < right:
             
            mid = (left + right) // 2

            if time_taken(mid) > h:
                left = mid + 1
            
            else:
                right = mid
        
        return left
        