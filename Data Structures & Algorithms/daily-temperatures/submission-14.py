class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        """
        [30,38,30,36,35,40,28]

        [1,0,0,0,0,0,0]

        [(38,1),(36,3)]

        condition: while t > stk[-1][0]: stk.pop(). Update the output[stk_idx] = current_idx - stk_idx
        """
        output = [0] * len(temperatures)
        stk = []

        for i, t in enumerate(temperatures):

            while stk and t > stk[-1][0]:

                stk_t, stk_i = stk.pop()

                output[stk_i] = i - stk_i

            stk.append((t,i))
        
        return output