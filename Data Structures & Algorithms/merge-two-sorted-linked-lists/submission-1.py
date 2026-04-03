# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #bruteforce 

        if list1 == None and list2 == None:
            return None

        list1_values = []
        curr = list1
        while curr:
            list1_values.append(curr.val)
            curr = curr.next
        
        list2_values = []
        curr = list2
        while curr:
            list2_values.append(curr.val)
            curr = curr.next
        
        combined_list = list1_values + list2_values
        combined_list.sort()

        head = ListNode(val= combined_list[0])
        curr = head
        for i in range(1, len(combined_list)):
            curr.next = ListNode(val= combined_list[i])
            curr = curr.next
        
        return head