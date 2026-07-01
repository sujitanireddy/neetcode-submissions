class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        """
        10  2        3          3  
        1   2        2          1
       car car      car        car
        0   1  2  3  4   5  6  7  8  9  10

        T = D/S

        [10,2,3]

        [(p,s)]

        """

        pos_speed = list(zip(position, speed))
        pos_speed.sort()
        stk = []
        
        for p, s in pos_speed:
            time_taken = (target - p) / s

            while stk and time_taken >= stk[-1]:
                stk.pop()

            stk.append(time_taken)

        if len(stk):
            return len(stk)
        
        else:
            return 0
        