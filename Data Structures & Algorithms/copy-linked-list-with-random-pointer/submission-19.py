"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
{
3: Node
7: Node
4: Node
}

Travere the linked list and create new nodees and add them to hashmap

{
old_node : new node
}

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        old_new_map = defaultdict()
        
        curr = head
        while curr:
            old_new_map[curr] = Node(curr.val)
            curr = curr.next
        
        for old, new in old_new_map.items():
            new.next = old_new_map.get(old.next)
            new.random = old_new_map.get(old.random)
        
        return old_new_map[head]

