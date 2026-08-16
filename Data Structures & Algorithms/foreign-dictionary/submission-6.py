"""
Notes:
- return "" if incorrect/false
- return increasing sorted letter
- 2 rules: 
    1. "hrn","hrf"    n -> f
    2. "abc" and "ab" : ab is a prefix of abc and len(abc) > len(ab): return ""

- Direct Graph
- AdjList List

{
  n : [f]
  h : [e]
  r : [n]
  e : [r]
}

[fn]

Topological Sort: Kahn's algorithm - Works on unconnected componets of a graph (have to verify)

[fnreh]
return reverse of this

"hrn","hrf","er","enn","rfnn"
 
h -> e -> r -> n -> f

TC: O(m*n*i)
SC: O(n)

m = max len of a word
n = no of words

TC of building the AdjList: O(m*n) 
TC for doing topological sort: O(i)

---------------------------------------

"er","enn"

{
  n : [f]
  h : [e]
  r : [n]
  e : [r]
}

processed = {}
visit = {}
res = [fn]


        {
            n : [f]
            h : [e]
            r : [n]
            e : [r]
            f : []
        }

            processed = {f,n,r,e,h}
            visit = {}
            res = [f,n,r,e,h]

"""


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        #builds a hashmap with all the unique char of the words list of strs with a empty set as value
        adjList = {c : set() for word in words for c in word}

        #building our adjlist
        for i in range(1,len(words)):
            A = words[i-1]
            B = words[i]

            length = min(len(A), len(B))

            #prefix check
            if A[:length] == B[:length] and len(A) > len(B): return ""

            for j in range(length):
                if A[j] != B[j]:
                    adjList[A[j]].add(B[j])
                    break
        
        res = []
        processed = set()
        visit = set()

        #Topological Sort with cycle detection
        def dfs(c):

            if c in visit:
                return False
            
            if c in processed:
                return True

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

        return "".join(res[::-1])


























        