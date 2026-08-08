# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        if not lists: return None

         1 -> 2 -> 4
         1 -> 3 -> 5 
         3 -> 6

        Algorithm:
            minHeap = [, ,(3,2,3), , (3,2,3)] #val, idx, node

        while minHeap: Keep popping
         
        1 -> 1 -> 2

        [[1][1][3]]

        n * log n
        k =len(lists) O(k)

        d -> 1 -> 
        """
        minHeap = []
        for i, node in enumerate(lists):
            heapq.heappush(minHeap, (node.val, i, node)) #val, idx, node
        
        dummy = ListNode()
        curr = dummy

        while minHeap:
            val, idx, node = heapq.heappop(minHeap)
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(minHeap, (node.val, idx, node))
        
        return dummy.next