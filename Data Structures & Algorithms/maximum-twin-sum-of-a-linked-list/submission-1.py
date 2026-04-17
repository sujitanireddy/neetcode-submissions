# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        fast, slow = head, head
        prev = None
        
        while fast and fast.next:

            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #slow = head of the second linked list
        #prev = head of the reversed linked list
        max_sum = 0
        
        while prev:

            max_sum = max(max_sum, prev.val + slow.val)

            prev = prev.next
            slow = slow.next
        
        return max_sum




        