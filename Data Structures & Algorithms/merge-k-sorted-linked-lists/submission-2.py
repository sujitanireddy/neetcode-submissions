# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        """
        1 -> 2 -> 4
        1 -> 3 -> 5
        3 -> 6

        [1,1,2,3,3,4,5,6]

        """
        heap = []
        dummy = ListNode()
        curr = dummy

        for i, node in enumerate(lists):
            heapq.heappush(heap,(node.val,i,node))
        
        heapq.heapify(heap)

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next 
            node = node.next

            if node:
                heapq.heappush(heap,(node.val,i,node))

        
        return dummy.next




        







        