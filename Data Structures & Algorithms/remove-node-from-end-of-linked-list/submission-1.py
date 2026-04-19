# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #Start the right pointer at the nth node from head by writing a loop
        #Start the left pointer at a node before head (dummy node) so that we land on nth - 1 node from the end

        dummy = ListNode(0, head)
        left = dummy
        right = head

        counter = 0
        while counter < n:
            right = right.next
            counter += 1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
    
        return dummy.next
        