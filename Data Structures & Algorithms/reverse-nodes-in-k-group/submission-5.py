# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #validate if there are even k nodes to reverse
        #if there are - then reverse and use recursion to point the .next 

        counter = 0
        curr = head

        while curr and counter < k:
            curr = curr.next
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