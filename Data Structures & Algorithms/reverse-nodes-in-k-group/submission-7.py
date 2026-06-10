# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #check if there are k nodes
            #If yes - reverse the k nodes
            #If not - Just return the original head
        
        #Use recursion to point the end of the linked list to the next reversed head


        counter = 0
        node = head
        while node and counter < k:
            node = node.next
            counter += 1
        
        if counter < k:
            return head
        
        curr = head
        prev = None
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head.next = self.reverseKGroup(node, k)

        return prev