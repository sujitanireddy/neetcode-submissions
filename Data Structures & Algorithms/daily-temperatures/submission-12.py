class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stk = []
        length = len(temperatures)
        output = [0] * length

        for i, t in enumerate(temperatures):

            while stk and t > stk[-1][0]:

                stk_t, stk_i = stk.pop()

                output[stk_i] = i - stk_i
            
            stk.append((t,i))
        
        return output