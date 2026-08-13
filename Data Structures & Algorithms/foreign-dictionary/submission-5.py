class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        """
        adjList
        {
            n : (f)       
            h : [e]
            r : [n]
            e : [r]
        }

        f -> n -> r -> e -> h

        a is prefix of b and a(len) < b(len)
        
        h -> e -> r -> n -> f
        """
        adjList = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            a = words[i]
            b = words[i+1]

            min_len = min(len(a), len(b))

            if len(a) > len(b) and a[:min_len] == b[:min_len]:
                return ""
            
            for j in range(min_len):
                if a[j] != b[j]:
                    adjList[a[j]].add(b[j])
                    break
        
        processed = set()
        visit = set()
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
            
            visit.remove(c)
            processed.add(c)
            res.append(c)

            return True

        
        for c in adjList.keys():
            if not dfs(c):
                return ""

        return "".join(res)[::-1]
        
        


