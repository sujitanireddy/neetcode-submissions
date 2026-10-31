# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #are there k values to reverse? 
        #base cases
        node = head
        i = 0
        while node and i < k:
            node = node.next
            i += 1
        
        if i < k:
            return head
        
        curr = head
        prev = None

        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = self.reverseKGroup(curr, k)

        return prev

        