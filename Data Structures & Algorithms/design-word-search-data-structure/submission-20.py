"""
                        d   b   m 
                    a       a       a
                y*          y*          y*

{
    d : {
          a : {
        }        y*: {   }
               }
}


"""
class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            
            curr = node

            for j in range(i, len(word)):

                c = word[j]

                if c == ".":

                    for node in curr.children.values():

                        if dfs(j+1, node):
                            return True

                    return False
                    
                else:

                    if c not in curr.children:
                        return False
                
                    curr = curr.children[c]
            
            return curr.word

        return dfs(0, self)
