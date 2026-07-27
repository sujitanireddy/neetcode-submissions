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
        
        """
        - Build the prefix tree. 
        - While traversing the board if a letter is found in the prefix tree then start searching
            - If we were able to traverse to the end of the prefix tree then we found the word 

        """
        root = TrieNode()
        for word in words:
            root.insert(word)
        
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        output = set()

        def dfs(r,c,node,word):

            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r,c) in visit:
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                output.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r,c,root,"")
        
        return list(output)