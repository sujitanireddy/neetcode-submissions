class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        while self.parent[n] != n:
            self.parent[n] = self.parent[self.parent[n]] #path halving/compression
            n = self.parent[n]
        return n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2: return False

        #union by rank
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        {
            0 : [1]
            1 : [0,2]
            2 : [1]
            3 : [4]
            4 : [3]
        }
        TC: O(V+E)
        SC: O(V+E)
        0 1 2 3 4
        
        0 - 2
        |
        1

        3 - 4
        """
        uf = UnionFind(n)
        res = n

        for u,v in edges:
            if uf.union(u,v):
                res -= 1
        
        return res


