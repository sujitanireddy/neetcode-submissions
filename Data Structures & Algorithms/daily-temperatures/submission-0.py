class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #base case
        if len(temperatures) <= 1:
            return [0]
        
        result = []

        for i in range(len(temperatures)-1):
            
            for j in range(i+1, len(temperatures)):

                if temperatures[j] > temperatures[i]:

                    result.append(j-i)

                    break

            else:
                
                result.append(0)

        result.append(0)
        
        return result






        

        