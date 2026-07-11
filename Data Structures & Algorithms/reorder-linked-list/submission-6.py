# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""  l2
2 -> 4 -> 6 -> 8 

l1                 l2
2 -> 4 -> Null.    8 -> 6      

F    t1         S
2 -> 10 -> N    4 -> 8 -> None

Algorithm
- Got to mid point. IF even then the last node of the first linked list
- Reverse the second half of the linked list
- Place pointers in first half and second half and keep reubilding the linked list.
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second = prev
        first = head

        while second:
            temp1 = first.next
            first.next = second
            temp2 = second.next
            second.next = temp1

            first, second = temp1, temp2
        
