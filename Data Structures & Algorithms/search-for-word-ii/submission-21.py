"""
Brute Force:
- TC: O(k * 4 ** (m * n))

Optimized Sol:
- Using Trie DS


                                        b    c      s
                                    a        a      t
                                t*   c       t*     a
                                       k*           c
                                         e          k*
                                            n
                                                d*

TC for inserting into a Trie: n * O(W) m*n

Overall TC: k * m*n

  ["a","b","c","d"]
  ["s","a","a","t"]
  ["a","c","k","e"]
  ["a","c","d","n"]

- Accumulate the word in the DFS
- If we go deep enough to find a end of a word then copy tha word over to res

{
    b : {a : {}}
}

"""
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

        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        visit = set()

        root = TrieNode()
        for word in words:
            root.insert(word)

        def dfs(r,c,word,node):
            
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r,c) in visit:
                return
            
            visit.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.word:
                res.add(word)

            dfs(r+1,c,word,node)
            dfs(r-1,c,word,node)
            dfs(r,c+1,word,node)
            dfs(r,c-1,word,node)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r,c,'',root)
        
        return list(res)








        









































