class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        output = [0] * n

        for i in range(n):

            current_temp = temperatures[i]

            for j in range(i+1, n):

                if temperatures[j] > current_temp:

                    break

            if temperatures[j] > current_temp:
                output[i] = j - i
        
        return output
        