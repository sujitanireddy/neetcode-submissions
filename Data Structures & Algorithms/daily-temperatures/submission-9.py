class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #if the stk is not empty and the incoming temp is > top of the stk then pop the top of the stk and save the diff in indexes in
        #output array

        n = len(temperatures)
        output = [0] * n
        stk = []

        for i, t in enumerate(temperatures):

            while stk and t > stk[-1][0]:

                stk_temp, stk_idx = stk.pop()

                output[stk_idx] = i - stk_idx  

            stk.append((t, i))
        
        return output
