class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0
        
    def find(self,n):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]] #path halving/compression 
            n = self.parent[n]
        return n

    def union_by_rank(self,n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2: return False #both parents are same, cycle detected.

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        
        else:
            self.parent[p1] = p2

        return True



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        """
        parents
        {
            1 : 1
            2 : 1
            3 : 1
            4 : 1
        }

        rank 
        {
            1 : 1
            2 : 0
            3 : 0
            4 : 0
        }

        1 <- 2
        ^ 4
        |
        3
        """
        n = len(edges)

        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union_by_rank(u,v):
                return [u,v]







