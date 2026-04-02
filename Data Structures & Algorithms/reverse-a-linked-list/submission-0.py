# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None
        
        node_values = []
        curr = head
        while curr:
            node_values.append(curr.val)
            temp = curr.next
            curr.next = None
            curr = temp
        
        head = ListNode(val = node_values[-1])
        curr = head 
        for i in range(len(node_values) - 2, -1, -1):
            curr.next = ListNode(val = node_values[i])
            curr = curr.next

        return head


        



        
        