class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def find(n):
            if n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        n = len(edges)

        parent = defaultdict()
        rank = defaultdict()
        for i in range(1, n+1):
            parent[i] = i
            rank[i] = 0

        for u, v in edges:

            p1, p2 = find(u), find(v)

            if p1 == p2: 
                return [u,v]
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            
            else:
                parent[p1] = p2
                rank[p2] += 1

            

