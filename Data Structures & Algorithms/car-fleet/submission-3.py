class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        veera_stk = []

        pos_speed = list(zip(position, speed))

        pos_speed.sort(reverse=True)

        for p, s in pos_speed:

            time_taken = (target - p) / s

            veera_stk.append(time_taken)

            if len(veera_stk) >= 2 and veera_stk[-1] <= veera_stk[-2]:

                veera_stk.pop()



        return len(veera_stk)



        