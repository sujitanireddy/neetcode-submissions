"""
                c
1 -> 2 -> 3 -> 4 -> 5 -> 6

1 <- 2 <- 3     4 <- 5 <- 6

3 -> 2 -> 1 -> 6 -> 5 -> 4

               t
   <- 1 -> 2 -> 3

algo
- are there k nodes to reverse?
    - if yes, reverse and recurse
    - if not just return

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        
        #validate if there are k nodes to reverse?
        count = 0
        curr = head
        while count < k and curr:
            curr = curr.next
            count += 1

        if count < k:
            return head
        
        #reverse the k nodes
        curr = head
        prev = None
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head.next = self.reverseKGroup(curr, k)

        return prev


