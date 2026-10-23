# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

L
     R                            
D -> 1 -> 2 -> 3 -> 4


     L
        R
D -> 5


Move R pointer n dist away from L and go unitl R reaches the end

L
    R
C
5

     L
        R
d -> 5

"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        L = R = dummy

        for i in range(n):
            R = R.next

        while R and R.next:
            L = L.next
            R = R.next
        
        L.next = L.next.next

        return dummy.next