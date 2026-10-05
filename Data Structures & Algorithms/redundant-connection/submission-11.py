"""
DFS with cycle detection
Union Find DS
TC: O(n)
SC: O(n)

"""
class UnionFind:
    def __init__(self,n):
        self.rank = {}
        self.parent = {}
        for i in range(1, n+1):
            self.rank[i] = 0
            self.parent[i] = i
        
    def find(self, n):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]] #path halving
            n = self.parent[n]
        return n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return False
        
        #union by rank
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1 

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uf = UnionFind(len(edges))

        for u, v in edges:
            if not uf.union(u,v):
                return [u,v]






































