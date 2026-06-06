# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #if k elemets are even present ot reverse

        node = head
        counter = 0

        while node and counter < k:
            node = node.next
            counter += 1
        
        if counter < k:
            return head
        
        #reverse the node
        prev = None
        curr = head

        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = self.reverseKGroup(node, k)

        return prev
        






