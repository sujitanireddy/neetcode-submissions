class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def find(n):
            while n != parent[n]:
                n = parent[n]
            return n

        n = len(edges)

        parent = defaultdict()
        for i in range(1, n+1):
            parent[i] = i
        
        print(parent)

        for u, v in edges:

            p1, p2 = find(u), find(v)

            print(p1, p2)

            if p1 == p2: 
                return [u,v]

            parent[p2] = p1

            print(parent)

            

