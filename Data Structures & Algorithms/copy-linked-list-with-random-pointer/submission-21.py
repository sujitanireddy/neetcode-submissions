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
        
        old_to_new = defaultdict()

        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        for old, new in old_to_new.items():
            new.next = None if not old.next else old_to_new[old.next]
            new.random = None if not old.random else old_to_new[old.random]

        return None if not old_to_new else old_to_new[head]