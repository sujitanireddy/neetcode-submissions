# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #algoritm
      #Add list nodes to heap and hepify
        # If the heap is not empty:
            #attach to curr
            #move pointer on that list node
        # heap push of the new node

        heap = []
        
        for i, node in enumerate(lists):
            heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        return dummy.next