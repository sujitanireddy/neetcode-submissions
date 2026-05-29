# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head
        fast = head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        prev = None 
        curr = slow.next
        slow.next = None     

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first = head
        second = prev
        max_twin_sum = 0

        while second:
            max_twin_sum = max(max_twin_sum, (first.val + second.val))
            first = first.next
            second = second.next
        
        return max_twin_sum
            

