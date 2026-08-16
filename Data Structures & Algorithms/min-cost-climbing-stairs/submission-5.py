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

Bottom up DP sol:
i
1,2,1,2,1,1,1
4 3 3 3 2

TC: O(n)
SC: O(1)

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        for i in range(len(cost) - 3, -1, -1):

            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
