class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def insert(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        ["a","b","c","d"]
        ["s","a","a","t"]
        ["a","c","k","e"]
        ["a","c","d","n"]
        w * 4***(m*n)
        Insert all our words to a Trie

                          b  c  s
                        a    a   t 
                    t*  c    t*    a
                          k*         c
                            e           k*
                              n
                                d*

        While exploring, build our words as well.
        """
        root = TrieNode()
        for word in words:
            root.insert(word)
        
        res = set()
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(r,c,node,word):

            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r,c) in visit:
                return
            
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.word:
                res.add(word)
            visit.add((r,c))

            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            
            visit.remove((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r,c,root,"")
        
        return list(res)




        

