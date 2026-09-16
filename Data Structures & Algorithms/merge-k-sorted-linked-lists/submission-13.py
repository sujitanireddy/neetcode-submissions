"""
      
[[1,2,4],[1,3,5],[3,6]]

[4,5,] (val,idx,node)

TC: O(n*m * log k)
SC: O(n)

     c
d -> 1 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        minHeap = [] #(val,idx,node)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy

        while minHeap:
            val, idx, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next

            if curr.next:
                heapq.heappush(minHeap, (curr.next.val, idx, curr.next))

        return dummy.next


























