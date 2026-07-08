class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        """ 
        hashamp = {num: chars}

        3
        d e f
        3 4 
        dg dh di eg eh ei fg fh fi

        """

        if not digits:
            return []

        hashmap = { '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        res = []
        sol = []

        def backtrack(i):

            #base case
            if i == len(digits):
                print(sol)
                res.append("".join(sol[:]))
                return
            
            for char in hashmap[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)

        return res
