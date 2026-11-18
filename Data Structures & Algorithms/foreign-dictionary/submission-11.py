"""
hrn hrf er enn rfnn
h -> e -> r -> n -> f
{
    n : f
    h : e
    r : n
    e : r
}
[f,n,r,e,h]

Algo:
- build adjlist while also chekcing prefix
- Topological sort
"""
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = {c : [] for word in words for c in word}

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            length = min(len(first), len(second))

            #prefix check
            if first[:length] == second[:length] and len(first) > len(second):
                return ""

            for j in range(length):
                if first[j] != second[j]:
                    adjList[first[j]].append(second[j])
                    break
            
        #topological sort
        visit = set()
        processed = set()
        res = []

        def dfs(node):

            if node in processed:
                return True
            
            if node in visit:
                return False

            visit.add(node)
            
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            
            visit.remove(node)
            processed.add(node)
            res.append(node)

            return True


        for src in adjList.keys():
            if not dfs(src):
                return ""
        
        return "".join(res[::-1])


