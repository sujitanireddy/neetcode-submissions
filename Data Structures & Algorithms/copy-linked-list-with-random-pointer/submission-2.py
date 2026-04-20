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
        
        hashmap = defaultdict()

        curr = head

        while curr:

            hashmap[curr] = Node(curr.val)

            curr = curr.next

        for old, new in hashmap.items():

            new.next = hashmap.get(old.next)
            new.random = hashmap.get(old.random)

        return hashmap[head]
        
        
        
        

            
