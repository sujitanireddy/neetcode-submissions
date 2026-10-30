class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            temp_res = []

            for j in range(1, len(temp)):
                temp_res.append(temp[j] + temp[j-1])
            
            res.append(temp_res)
        
        return res

