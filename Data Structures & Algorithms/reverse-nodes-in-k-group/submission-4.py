# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #algorithm

        #Check if there are k node
        # if not just return the head
        # if k nodes exists:
            #reverse
        # Use recursion to get the head.next
        #retrurn prev

        node = head
        counter = 0

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
