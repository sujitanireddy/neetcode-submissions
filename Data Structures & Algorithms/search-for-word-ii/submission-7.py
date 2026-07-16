class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            root.insert(word)

        ROWS = len(board)
        COLS = len(board[0])
        output = set()
        visited = set()

        def dfs(r, c, root, word):

            curr = root
            if r < 0 or c < 0 or r == ROWS or c == COLS or ((r,c) in visited) or board[r][c] not in curr.children:
                return
            
            visited.add((r,c))
            curr = curr.children[board[r][c]]
            word += board[r][c]
            
            if curr.word == True:
                output.add(word)

            dfs(r+1, c, curr, word) 
            dfs(r-1, c, curr, word) 
            dfs(r, c+1, curr, word)
            dfs(r, c-1, curr, word)

            visited.remove((r,c))
 
        for r in range(ROWS):
            for c in range(COLS):
                    dfs(r, c, root, "")
            
        return list(output)










