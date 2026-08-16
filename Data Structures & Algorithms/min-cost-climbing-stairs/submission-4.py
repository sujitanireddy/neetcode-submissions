"""
Notes:
- can start at index 0 or 1

 0,1,2,3,4,5,6
[1,2,1,2,1,1,1]

                                             1
                                        2          1
                                    1      2     2    1
                                 1     1                1 

                                    
f(i) = cost[i] + min(f(i+1), f(i+2))
Base case: if i >= len(cost): return 0

BruteForce: 
TC: O(2**n)
SC: O(h)

Top Down Memoiztion:
TC: O(n)
SC: O(n)

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}
        
        def recurse(i):

            #basecase 
            if i >= len(cost):
                return 0
            
            if i in cache:
                return cache[i]

            cache[i] = cost[i] + min(recurse(i+1), recurse(i+2))

            return cache[i]
        
        recurse(0)

        return min(cache[0], cache[1])
