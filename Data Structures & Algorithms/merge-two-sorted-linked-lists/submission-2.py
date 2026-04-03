# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #algorithm
        #Use a dummy node as curr and validate if dummy.next should be list1 or list2 and move list1 or list2 pointer based on that.
        #Once you are at the end of the list of either 1 or 2 then link the remainder of list1 or list2 to the curr.

        d = ListNode()
        curr = d

        #both nodes exists
        while list1 and list2:

            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = curr.next
            
            else:
                curr.next = list2
                curr = list2
                list2 = curr.next
        
        curr.next = list1 if list1 else list2

        return d.next
        




