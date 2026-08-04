class WordDictionary:

    """
    . a y
    b . .

    root : {d : {a : {y*: {}}}
            b : {a : {y*: {}}}
            m : {a : {y*: {}}}}

    Iterate over all the children at that node's level in the tire and try all possible paths to see if there is a match.

    """

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

        def dfs(i,node):

            curr = node
            for j in range(i, len(word)):

                c = word[j]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.word

        return dfs(0,self)