# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find mid point (the tail of first half of linked list)
        #Reverse the second half of the linked list in place
        #Merge both

        fast = head.next
        slow = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None
        
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




