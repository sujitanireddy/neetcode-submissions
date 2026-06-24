# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #Validate if there are k nodes, if there are then reverse else don't
        counter = 0
        node = head
        while node and counter < k:
            node = node.next
            counter += 1
        
        if counter < k:
            return head
        
        #reverse the node
        curr = head
        prev = None
        
        for _ in range(k):
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        
        #Use recursion to point the tail node to the head of the reversed linked list
        head.next = self.reverseKGroup(node, k)

        return prev

        