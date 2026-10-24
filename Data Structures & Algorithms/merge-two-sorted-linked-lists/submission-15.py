# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
        l1
1   ->   2    -> 4

        l2
1   ->   3    -> 5

d -> 1 -> 1


Notes:
- When l1 or l2 goes out of bounds, apppend the reamning list
- if not l1 and not l2: return None
- if l1 and not l2: return l1
- if l2 and not l1: return l2

"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        if list1:
            curr.next = list1
        
        if list2:
            curr.next = list2
        
        return dummy.next
        

            
