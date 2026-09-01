"""
target = 10, position = [4,1,0,7], speed = [2,2,1,1]

     1      2       3      4      5      6      7     8      9
0------------------------------------------------------------------10
C@1 C@2                   C@3                  C@1
T#10T#4.5                 T#2                  T#3

stk = [3]

stk[0] > time: stk.pop()
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = sorted(list(zip(position, speed)), reverse = True)

        stk = []

        for p, s in pos_speed:

            t = (target - p) / s

            stk.append(t)

            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
            
        return len(stk)