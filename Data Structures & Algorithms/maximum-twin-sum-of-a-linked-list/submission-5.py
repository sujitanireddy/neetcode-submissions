# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        """
        - Got to mid point
        - Reverse the second half of the linked list
        - Add 1st and 2nd half and keep max_so_far
        """

        max_twin_sum = 0
        slow = head 
        fast = head.next

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

        while second:
            max_twin_sum = max(max_twin_sum, (head.val + second.val))
            second = second.next
            head = head.next
        
        return max_twin_sum
            
