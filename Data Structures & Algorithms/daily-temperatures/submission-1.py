class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        length = len(temperatures)
        result = [0] * length

        for i in range(length):
            for j in range(i+1, length):
            
                if temperatures[j] > temperatures[i]:

                    result[i] = j - i

                    break
        
        return result
        