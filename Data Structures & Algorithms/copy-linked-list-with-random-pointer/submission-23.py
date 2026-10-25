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

        if not head:
            return None
        
        old_to_new = defaultdict()

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        for old, new in old_to_new.items():
            old_to_new[old].next = old_to_new.get(old.next, None)       
            old_to_new[old].random = old_to_new.get(old.random, None) 
        
        return old_to_new[head]