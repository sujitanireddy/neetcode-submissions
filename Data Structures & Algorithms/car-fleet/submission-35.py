class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        """
        Observations: one lane highway

    pos    0   1   2   3   4   5   6   7   8   9   10                              
    spe    1   2           2           1
    tim    10  4.5         3           3
           ------------------------------------------
        

        time is same or small we pop form stk
        
        3

        

        """

        pos_speed = list(zip(position, speed))
        pos_speed.sort(reverse=True)

        stk = []

        stk.append((target - pos_speed[0][0])/pos_speed[0][1])

        for p, s in pos_speed:

            time = (target - p) / s

            while stk and time > stk[-1] :
                stk.append(time)
        
        return len(stk)
