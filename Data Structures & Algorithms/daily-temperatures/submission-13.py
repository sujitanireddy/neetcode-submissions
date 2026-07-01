class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        """
        [30,38,30,36,35,40,28]
        [1,4,1,2,1,0,0]

        []

        """

        output = [0] * len(temperatures)
        stk = [] #[(temp, idx)]

        for i, t in enumerate(temperatures):

            while stk and t > stk[-1][0]:

                stk_temp, stk_idx = stk.pop()

                output[stk_idx] = i - stk_idx

            stk.append((t,i))
        
        return output