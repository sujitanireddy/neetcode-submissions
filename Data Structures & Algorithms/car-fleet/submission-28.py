class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = sorted(zip(position, speed), reverse=True)

        print(pos_speed)

        stk = []

        for p, s in pos_speed:

            time_taken = (target - p) / s

            stk.append(time_taken)

            print(time_taken)

            if len(stk) >= 2 and stk[-2] >= stk[-1]:

                stk.pop()
        
        return len(stk)


       