"""
Observations:
- We always want to optimize to min cost - No 1 priority
- While adhering to the constrains of our problem. 
 0 1 2 3
[1,2,3,4]

L R
0 1 2 3 4 5 6
1,2,1,2,1,1,1                                   1 + min ( f(2), f(1) )
                                                            |

                                                            1 + min ( f(3), f(4) )
                                                                        |
                                                                      
                                                                      2 + min ( f(4), f(5))

                                                                                 |

                                                                                 1 + min ( 1, f(5))

                                                                                                |

                                                                                                1 + min ()

        
i >= len(cost):
    return 0

f(n) = cost[i] + f(min(cost[i+1],cost[i+2])).idx(nums)

start 0th or 1st idx
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])






