# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        """
               L         R                 
     D -> 1 -> 2 -> 3 -> 4
        """
        dummy = ListNode(0,head)
        L = R = dummy

        for i in range(n):
            R = R.next
        
        while R and R.next:
            L = L.next
            R = R.next
        
        L.next = L.next.next

        return dummy.next

