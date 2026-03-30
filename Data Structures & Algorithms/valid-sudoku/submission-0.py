class Solution:

    def sub_square(self, board, start_index_i, end_index_i, start_index_j, end_index_j):
        seen_sub_square = set()
        for i in range(start_index_i,end_index_i):
            for j in range(start_index_j,end_index_j):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen_sub_square:
                    return False
                seen_sub_square.add(board[i][j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Not a valid board
        if len(board) != 9:
            return False
        
        #Each row must contain the digits 1-9 without duplicates.

        for row in board:
            seen = set()
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
            #print(seen)
        
        #Each column must contain the digits 1-9 without duplicates

        for i in range(len(board)):
            seen_column = set()
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen_column:
                    return False
                seen_column.add(board[j][i])
            #print(seen_column)
        

        #Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates
        start_index_i = 0
        end_index_i = 9
        start_index_j = 0
        end_index_j = 9

        for i in range(start_index_i, end_index_i, 3):

            for j in range(start_index_j, end_index_j, 3):

                if not self.sub_square(board, i ,i+3, j, j+3):

                    return False

        return True