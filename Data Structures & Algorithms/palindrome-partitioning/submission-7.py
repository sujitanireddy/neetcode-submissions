"""                             0   1    2
                                a   a    b

                            [a]       [aa]      aabX
                        
                        [a,a]          [aa,b]  

                    [a,a,b]   


SC: O(n)
TC: 2**n
 
0 1 2
a a b


j = 0
i = 0, 1, 2

i = 1
j = 0


i = 1, 2 

i = 1
j = 2

i = 2
j = 3


"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        sol = []

        def backtrack(i):

            if i >= len(s):
                res.append(sol.copy())
                return

            for j in range(i, len(s)):
                
                string = s[i:j+1]

                if string[::-1] == string:
                    sol.append(string)
                    backtrack(j+1)
                    sol.pop()


        backtrack(0)
        return res




