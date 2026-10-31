# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        L = R = dummy
        
        for _ in range(n):
            R = R.next
        
        while R.next:
            L = L.next
            R = R.next
        
        L.next = L.next.next

        return dummy.next