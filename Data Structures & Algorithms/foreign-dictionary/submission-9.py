"""
words = []

if claim in incorrect: return "" else return string of unique letters

         i     
["hrn","hrf","er","enn","rfnn"]

h -> e -> r -> n -> f -> h

TC: O(m*n)
SC: O(m*n)

Adjlist

{
    n : [f]
    h : [e]
    r : [n]
    e : [r]
}

processed = 
visit = {n,f}

[f,n

fnreh
Topological sort
"""
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = {}
        for word in words:
            for i in range(len(word)):
                adjList[word[i]] = []

        res = []
        visit = set()
        processed = set()

        #building the adjList
        for i in range(1, len(words)):

            a, b = words[i-1], words[i]
            a_length, b_length = len(a), len(b)
            length = min(a_length, b_length)

            if a_length > b_length and a[:b_length] == b:
                return ""

            for j in range(length):
                if a[j] != b[j]:
                    adjList[a[j]].append(b[j])
                    break

        def dfs(c):

            #base cases
            if c in processed:
                return True

            if c in visit:
                return False

            visit.add(c)
            
            for nei in adjList[c]:
                if not dfs(nei):
                    return False
            
            res.append(c)
            processed.add(c)
            visit.remove(c)

            return True

        
        for c in adjList.keys():
            if not dfs(c):
                return ""
        
        return "".join(res)[::-1]








































