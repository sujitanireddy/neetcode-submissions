"""
["hrn","hrf","er","enn","rfnn"]

h -> e -> r -> n -> f

{
    n : [f]
    h : [e]
    r : [n]
    e : [r]
}
fnreh
TC: O(V+E)
SC: O(V+E)

"""
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = {c : set() for word in words for c in word}

        for i in range(len(words) - 1):
            A = words[i]
            B = words[i+1]

            min_length = min(len(A), len(B))

            if len(B) < len(A) and A[:min_length] == B[:min_length]:
                return ""

            for j in range(min_length):
                if A[j] != B[j]:
                    adjList[A[j]].add(B[j])
                    break
        
        visit = set()
        processed = set()
        res = []

        def dfs(c):
            
            if c in processed:
                return True

            if c in visit:
                return False 
            
            visit.add(c)

            for nei in adjList[c]:
                if not dfs(nei):
                    return False

            res.append(c)
            visit.remove(c)
            processed.add(c)

            return True


        for c in adjList.keys():
            if not dfs(c):
                return ""

        return "".join(res[::-1])









