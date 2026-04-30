class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)

        stk = []

        for i, t in enumerate(temperatures):

            while stk and t > stk[-1][0]:

                stk_temp, stk_idx = stk.pop()

                output[stk_idx] = (i - stk_idx)
            
            stk.append((t, i))
        
        return output