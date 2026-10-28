"""
rows
{
    (rows,0) :
    (cols,0) : 
    (squares, r//3, c//3) : 
}
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        visit_map = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                if board[r][c] in visit_map[("rows",r)] or board[r][c] in visit_map[("cols",c)] or board[r][c] in visit_map[("squares", r//3, c//3)]:
                    return False
                
                visit_map[("rows",r)].add(board[r][c])
                visit_map[("cols",c)].add(board[r][c])
                visit_map[("squares", r//3, c//3)].add(board[r][c])
        
        return True
                
                