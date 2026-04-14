# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy

        while list1 and list2:

            if list2.val <= list1.val:
                head.next = list2
                head = list2
                list2 = list2.next 

            else:
                head.next = list1
                head = list1
                list1 = list1.next

        if not list1:
            head.next = list2
        
        else:
            head.next = list1

        return dummy.next