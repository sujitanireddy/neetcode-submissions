"""
rows = 3

G   L   H   N
O G E S I I G
O   I   R

rows = 4

G    I   
O  E 
O L  
G    

    r
    i
G   O   O   G   L   E   I   S   H   I   R   I   N   G


Notes:
- last row and first row we can caputer using this formule = step = (2 * rows) - 2
- for middle rows = step - (r * 2)

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows <= 1:
            return s

        res = ""

        for r in range(numRows):

            step = (2 * numRows) - 2

            for i in range(r, len(s), step):

                res += s[i]

                if r > 0 and r < (numRows - 1) and (i + (step - (r * 2))) < len(s):

                    res += s[i + (step - (r * 2))]
        
        return res


