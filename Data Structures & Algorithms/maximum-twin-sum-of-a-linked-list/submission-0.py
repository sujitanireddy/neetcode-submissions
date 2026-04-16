# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast, slow = head, head
        prev = 0
        
        while fast and fast.next:

            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #prev = head of first half of reversed linked list
        #slow = head of the second half of the linked list

        max_twin_sum = 0
        while prev and slow:

            max_twin_sum = max(max_twin_sum, prev.val + slow.val)

            prev = prev.next
            slow = slow.next

        return max_twin_sum
                    






            
