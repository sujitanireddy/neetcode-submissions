"""
E = V**2 (Complete Graph)
E = V - 1 (no cycle)

Represent my graph using AdjList
DFS - visit all the nodes

O(n ** 2)
O(n)

1 - 3  
| 4  
2           (union by rank also include path halving/compression)

TC: O(n)
SC: O(n)

{
  1 : 1
  2 : 1
  3 : 1
  4 : 1
}

"""
class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {} #height of the tree
        for i in range(1, n+1):
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        uf = UnionFind(n)

        for src, des in edges:
            if not uf.union(src,des):
                return [src, des]





        