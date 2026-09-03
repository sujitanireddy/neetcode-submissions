"""
   S
       F
[5,4,2,1]

L                   R
5 -> 4         2 <- 1

Brute Force:
TC: O(n)
SC: O(n)

Optimal:
TC: O(n)
SC: O(1)

Algorithm:
- S = 0, F = 1
- Find mid point
- Point the tail of the first section to null
- Reverse the second half of the linked list
- Move the pointers to get your max sum while computing and keeping a max so far value
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = None
        slow.next = None

        #reverse the linked list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first = head
        second = prev

        max_sum = 0
        while first:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_sum













































