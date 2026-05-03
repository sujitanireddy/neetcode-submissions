class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #pos =   [4,1,0,7]
        #speed = [2,2,1,1]
                 
        # 10 9 8 car 6 5 car 3 2 car car
        #         1       2       2   1 
        #         3       3      4.5  10 

        # 12 11 car 9 car 7 6 car 4 car 2 1 car
        #.      2      4       1     3        1
        #.      1      1       7     3       12

        pos_speed = sorted((zip(position, speed)), reverse=True)

        stk = []

        for p, s in pos_speed:

            time = (target - p) / s

            stk.append(time)

            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)