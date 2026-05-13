"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        """
        (3,next,random) -> (7,next,random) -> (4,next,random) -> (5,next,random) -> null

        old_to_new =   {(3,next,random): (3),     (new_node.next = old_to_new.get(old.next))
                        (7,next,random): (7),
                        (4,next,random): (4),
                        (5,next,random): {5}
                        }
        """

        if not head:
            return None

        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        for old_node, new_node in old_to_new.items():
            new_node.next = old_to_new.get(old_node.next)
            new_node.random = old_to_new.get(old_node.random)
        
        return old_to_new[head]