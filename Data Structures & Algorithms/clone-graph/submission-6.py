"""
1 - n

early return: if not node

old:
 1  <->  2   -> 3
(2)    (1,3)   (2)

new:
 1  ->  2  ->  3
(2)    (1,3)  (2)

traveral algorithm = dfs

TC: O(V+E)
SC: O(V)

{
  1 : 1
  2 : 2
  3 : 3
}


old:
 1  <->  2  <-> 3
(2)    (1,3)   (2)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: return
        
        oldTonew = defaultdict()

        def dfs(node):

            if node in oldTonew:
                return oldTonew[node]

            new_node = Node(node.val)
            
            oldTonew[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node)


"""
old:
 1  <->  2  <-> 3
(2)    (1,3)   (2)

new: 
 1*       2*        3*
(2*)     (1*, 2*)     (2*)

{
   1 : 1*
   2 : 2*
   3 : 3*

}

"""











