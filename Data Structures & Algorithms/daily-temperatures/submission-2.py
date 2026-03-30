class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and stack[-1][0] < t:

                stack_temp, stack_idx = stack.pop()

                result[stack_idx] = i - stack_idx

            stack.append((t,i)) 
        
        return result


        