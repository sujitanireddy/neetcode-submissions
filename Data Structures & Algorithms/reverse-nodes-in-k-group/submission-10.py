# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        """
        1. validate if there are k nodes to reverse.
            - If yes - Reverse the k nodes
            - return as is
        
        2. Reversing a linked list

        3. Recursivly go and reverse the next k nodes and use that return value to tie it back to the previouslhy reversed linked list
        
        """

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
        
        head.next = self.reverseKGroup(node, k)

        return prev

        
