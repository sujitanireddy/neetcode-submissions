class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        TC : O(n) * Inverse Ackreman Function (almost constant)
        SC : O(v+e)
        """
        
        #Build forest of nodes
        n = len(edges)
        parent = {}
        rank = {}
        for i in range(1, n+1):
            parent[i] = i
            rank[i] = 0
        
        #Find for root of the tree
        def find(n):
            while n!= parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n
        
        for u, v in edges:
            
            p1, p2 = find(u), find(v)

            if p1 == p2: return [u,v]

            #union by rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p2] += 1


