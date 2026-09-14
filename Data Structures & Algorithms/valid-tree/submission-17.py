"""
0 
|
1 

[1,4]

{
    0 : 1,2,3
    1 : 0,4
    2 : 0
    3 : 0
    4 : 1
}
two ways: 
- Union find DS, where if we are not able to union. Cycle detected 
- DFS to see if all nodes are visited. No need to check cycle

early return case:
- if len(edges) >= n: return False
"""
class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    #method to find the parent
    def find(self,n):
        while self.parent[n] != n:
            self.parent[n] = self.parent[self.parent[n]] #path halving
            n = self.parent[n]
        return n

    def union(self,n1,n2):

        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        
        else:
            self.parent[p1] = p2
            self.rank[p1] += 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) >= n: 
            return False
        
        uf = UnionFind(n)

        for u,v in edges:
            if not uf.union(u,v):
                return False
        
        return len(edges) == n-1





























