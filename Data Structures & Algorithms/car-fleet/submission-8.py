class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = list(zip(position, speed))
        pos_speed.sort(reverse=True)
        stk = []
        print(pos_speed)

        for p, s in pos_speed:
            time_taken = (target - p) / s
            stk.append(time_taken)

            print(stk)

            while len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        
        return len(stk)

