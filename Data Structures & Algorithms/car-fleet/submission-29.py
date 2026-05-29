class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stk = []

        pos_speed = sorted(zip(position, speed), reverse = True)

        for p, s in pos_speed:

            time_taken = (target - p) / s

            stk.append(time_taken)

            while len(stk) >= 2 and stk[-1] <= stk[-2]:

                stk.pop()
        
        return len(stk)
            

