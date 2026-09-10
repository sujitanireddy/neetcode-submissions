"""

                                        3 4

                                    d     e       f
                            
                            dg  dh  di

edge case:
- if not digits: return []

"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits: return []
        
        num_letter_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        res = []
        sol = []

        def backtrack(i):

            if len(digits) == len(sol):
                res.append("".join(sol))
                return

            for char in num_letter_map[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)

        return res




            
        



