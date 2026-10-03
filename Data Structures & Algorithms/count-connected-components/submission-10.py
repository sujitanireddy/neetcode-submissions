"""
4
0 ----- 1 -------2
3 ------ 4

4
0 --------- 1 -------- 2 -------- 3 ------ 4

{
    0 : [1]
    1 : [0,2]
    2 : [1]
    3 : [4]
    4 : [3]
}

visit = {0,1,2,3,4}


1 + dfs(0)
1 + dfs(3)

O(V+E)
O(V)

---------------------------------------------------------
Disjoint set (union find)

0   1   2   3   4


    0 
    |
    |
    1


1, 2

TC: O(n) O(1)
SC: O(n)

2 methods
- Union (union by rank)
- Find

rank                        
{
    0: 0
    1: 0
    2: 0
    3: 0
    4: 0
}

parent
{
    0: 0
    1: 1
    2: 2
    3: 3
    4: 4
}


1 != 0
n = 0

0 != 0
"""

class UnionFind:
    def __init__(self,n):
        self.rank = {}
        self.parent = {}

        for i in range(n):
            self.rank[i] = 0
            self.parent[i] = i

    def find(self,n):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]] #path halving
            n = self.parent[n]
        return n

    def union(self,n1,n2):

        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2: #cycle detection
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        res = n
        uf = UnionFind(n)

        for u,v in edges:
            if uf.union(u,v):
                res -= 1
        
        return res



















        