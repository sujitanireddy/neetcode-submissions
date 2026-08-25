"""
None             prev
     <- 1 -> 2 -> 3 -> 4 -> 5 -> 6
                       c

3 -> 2 -> 1

if < k: return head
reverse the linked list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #Check if we have atleast k nodes
        curr = head
        counter = 0
        while curr and counter < k:
            curr = curr.next
            counter += 1
        
        #if less than k nodes, just return head
        if counter < k:
            return head
        
        #reverse the linked list
        prev = None
        curr = head
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = self.reverseKGroup(curr, k)

        return prev




        
