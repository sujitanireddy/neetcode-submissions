class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        """ 

          d                 e                  f

    g   h.   i     g.      h.      i      g.  h.    i


        n = len(digits)
        TC: O(n ** 4)

        hashmap = {'2' : 'abc'}

        for every num in digits:
            lookup in the hashmap

        """
        if not digits:
            return []

        telephone_map = { '2' : 'abc', '3' : 'def', '4':'ghi', '5':'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        sol = []

        def backtrack(i):

            if i > len(digits):
                return

            if len(digits) == len(sol):
                res.append("".join(sol))
                return

            for char in telephone_map[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()

        backtrack(0)

        return res