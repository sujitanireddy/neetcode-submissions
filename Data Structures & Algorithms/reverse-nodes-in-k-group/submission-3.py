# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #we have to validate if k nodes are present.
            #if present -> reverse and the head.next will be resolved by recursion
            #if not present just return head
        
        counter = 0
        node = head
        while node and counter < k:
            node = node.next
            counter += 1
        
        if counter < k:
            return head
        
        prev = None
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = self.reverseKGroup(curr, k)
        
        return prev