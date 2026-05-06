# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #traverse till k
        #if less than k: return the head
        #Reverse the k elements
        #Use recursion to resolve the head.next
        #return the prev

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

        head.next = self.reverseKGroup(curr,k)

        return prev
            