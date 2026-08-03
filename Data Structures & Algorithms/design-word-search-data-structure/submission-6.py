"""
Trie DS
- Build a trienode class. children ={}, word = False
                                d  b   m
                            a      a     a
                        y*         *y      *y

If we encounter ".", do a dfs on all the children at that level.
"""
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

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:

        def dfs(j,node):

            curr = node

            for i in range(j, len(word)):

                c = word[i]

                if c == ".":

                    for child in curr.children.values():

                        if dfs(i+1, child):
                            return True
                    
                    return False

                else:

                    if c not in curr.children:
                        return False
                
                    curr = curr.children[c]
            
            return curr.word

        
        return dfs(0,self.root)
        
