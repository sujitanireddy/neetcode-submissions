"""
[
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]

avg len word in words = l
no of words = n

Brute force approach:
O(n*lm*n) = O(n**4)

                                    root
                               b     c    s
                            a        a    t
                         t*  c       t*   a
                              k*          c
                               e          k*
                                n 
                                 d*

Trie approach:
TC: O(n**2)
SC: O(l)

set() to store out output but return as list at the end

            visit: {(0,1)}
            word: "b"

               0.  1.  2.  3         
            0["a","b","c","d"]
            1["s","a","a","t"]
            2["a","c","k","e"]
            3["a","c","d","n"]
            

                                      root
                               b     c    s
                            a        a    t
                         t*  c       t*   a
                              k*          c
                               e          k*
                                n 
                                 d*


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

        root = TrieNode()
        for word in words:
            root.insert(word)

        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        visit = set()

        def dfs(r,c,node,word):
            
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] not in node.children:
                return

            visit.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.word:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r,c,root,'')

        return list(res)
        
"""





            visit: {(0,1)}
            word: "b"

               0.  1.  2.  3         
            0["a","b","c","d"]
            1["s","a","a","t"]
            2["a","c","k","e"]
            3["a","c","d","n"]
            

                                      root
                               b     c    s
                            a        a    t
                         t*  c       t*   a
                              k*          c
                               e          k*
                                n 
                                 d*

"""


        