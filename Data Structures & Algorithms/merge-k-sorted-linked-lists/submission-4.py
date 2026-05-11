# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #algorithm 
            #add the list nodes to a heap and heapify (o(n))
            # create a dummy node and use curr as a pointer to add nodes to dummy node
                #take min attach to dummy node. 
                    #move curr
                    #move node
        
        heap = []
        for i, node in enumerate(lists):
            heapq.heappush(heap, (node.val, i, node))
        
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