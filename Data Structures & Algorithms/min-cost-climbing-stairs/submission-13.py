"""
             
0 1 2 
1,2,3
                      
1,2,1,2,1,1,1

TC: O(2**n)
SC: O(h)

Recurence Relation
f(n) = cost[i] + min(f(i+1), f(i+2))

0 1 2 3 4 5 6
1,2,1,2,1,1,1
      3 2

7
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        for i in range(len(cost) -3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0],cost[1])
        