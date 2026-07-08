# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        """
             c    n
        d -> 1 -> 2 -> 4

        L2
        1 -> 3 -> 5

        L3
        3 -> 6

             c
        d -> 1

        minheap = min of the value
        minheap = [1,1,3] #(node.val, idx, node)
        while heap:
        """

        dummy = ListNode()
        curr = dummy
        minheap = []
        for i, node in enumerate(lists):
            heapq.heappush(minheap, (node.val, i, node))
        
        heapq.heapify(minheap)

        print(minheap)

        while minheap:
            val, idx, node = heapq.heappop(minheap)
            print(val, idx, node)
            curr.next = node
            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(minheap, (node.val, idx, node))
            
        return dummy.next

