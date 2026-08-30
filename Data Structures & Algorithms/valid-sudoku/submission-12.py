class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hashmap = defaultdict(set)

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue
                
                if val in hashmap[("row",r)] or val in hashmap[("col",c)] or val in hashmap[(r//3,c//3)]:
                    return False
                
                hashmap[("row",r)].add(val)
                hashmap[("col",c)].add(val)
                hashmap[(r//3,c//3)].add(val)
        
        return True