# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #find the mid point of the linked list -> F and S pointer
        #Reverse the second half of the linked list
        #iteratre over first and second half and keep joining them

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        
        first = head
        second = prev

        while second:

            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2
    
            


                  
        #2 -> 4 -> None     8 -> 6

