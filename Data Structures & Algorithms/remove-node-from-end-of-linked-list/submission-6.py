# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        """

                      R              
        dummy -> 1 -> 2 -> 3 -> 4

        Land on (n-1)th

        """

        dummy = ListNode()
        dummy.next = head
        
        L = R = dummy

        for _ in range(n):
            R = R.next
        
        print(R.val)
        
        while R.next:
            L = L.next
            R = R.next
        
        print(L.val)
        
        L.next = L.next.next

        return dummy.next


 