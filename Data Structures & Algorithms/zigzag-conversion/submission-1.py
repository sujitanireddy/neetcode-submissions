class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows <= 1:
            return s

        res = []

        for i in range(numRows):

            step = (numRows - 1) * 2

            for j in range(i, len(s), step):

                res.append(s[j])
            
                if i > 0 and i < (numRows - 1) and (j + (step - (i * 2))) < len(s):

                    res.append(s[j + (step - (i * 2))])
        
        return "".join(res)
