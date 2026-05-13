# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #BruteForce. TC: O(n), SC: o(n)

        # Algorithm -> Initiate a L pointer a dummy node and attach the dummy node to the head.
        # Initate a R pointer n distance away from dummy node
        # Increment R and L until R or R.next is None
        # Move pointers to del the nth node

        dummy = ListNode()
        dummy.next = head
        L = R = dummy

        counter = 0
        while counter < n:
            R = R.next
            counter += 1
        
        while R and R.next:
            R = R.next
            L = L.next
        
        #delete the node.
        L.next = L.next.next

        return dummy.next
