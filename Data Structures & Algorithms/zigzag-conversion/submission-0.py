class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows <= 1:
            return s
        
        res = []

        for r in range(numRows):

            step = (numRows - 1) * 2

            for i in range(r, len(s), step):
                
                res.append(s[i])

                if r > 0 and r < (numRows - 1) and i + step - 2 * r < len(s):

                    res.append(s[i + step - 2 * r])
        
        return "".join(res)

