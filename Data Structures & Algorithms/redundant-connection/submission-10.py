class UnionFind:
    def __init__(self,n):
        self.parent = {} #node:parent relationship
        self.rank = {} #height of the tree

        for i in range(1,n+1):
            self.parent[i] = i
            self.rank[i] = 0
    
    #Given a node, return the root
    def find(self,n):
        while self.parent[n] != n:
            self.parent[n] = self.parent[self.parent[n]] #path halving/compression
            n = self.parent[n]
        return n 

    #Given two nodes, returns true if they can be unioned else false
    def union(self,n1,n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False

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

        n = len(edges)
        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union(u,v):
                return [u,v]




        