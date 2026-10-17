"""          
gas =  [1, 2,3,4]

               i
cost = [2, 2,4,1]
       [-1,0,-1,3]

TC: O(n**2)

Early return:
if sum(gas) < sum(cost):
    return -1

if the diff is -ve move idx forward


"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        res = 0
        total = 0

        for i in range(len(gas)):

            total += (gas[i] - cost[i])

            if total < 0:
                res = i + 1
                total = 0
        
        return res