# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        heapq.heapify(heap)

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



        