class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        pos_speed = list(zip(position, speed))

        pos_speed.sort(reverse=True)

        for p, s in pos_speed:

            time_taken = (target - p) / s

            stack.append(time_taken)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:

                stack.pop()

        return len(stack)


       
        



        