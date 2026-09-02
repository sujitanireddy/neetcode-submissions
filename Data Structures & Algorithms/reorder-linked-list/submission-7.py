"""
                   T1

     F      T2     S        
2.   4     None <- 6    8

     S
              F
2 -> 8 -> 4 -> 6

                      
     f                     s    s
2 -> 4 ->     Nonee <- 6 <- 8 <- 10

2 -> 10

Find mid point
Reverse the second half of the linked list
Iterate on the second portion while weaving the front and back linked list

TC: O(n)
SC: (1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next, prev = None, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second = prev
        first = head

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

