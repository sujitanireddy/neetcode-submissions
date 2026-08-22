"""
i
1 2 3    
3 2 3

        i 
1,2,1,2,1,1,1

f(i) = cost[i] + min(f(i+1), f(i+2)) 

base case: i >= len(cost): return 0

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for i in range(len(cost) - 3, -1, -1):

            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0],cost[1])


        
