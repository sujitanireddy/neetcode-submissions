"""
{   
    1 : (1,30)
    2 : (2,20)
    3 : (3,30)
}
 
  
head <-> (2,20) <-> tail

(1,30)

helper methods nedded:
- add_to_head
- remove_node

put - have to check conflict for capacity

get - remove and attached to head
put - attach to head/ cacpacity check


"""
class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode(0,0) #MRU
        self.tail = ListNode(0,0) #LRU

        self.head.next = self.tail
        self.tail.prev = self.head 

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        
        new_node = ListNode(key,value)
        self.cache[key] = new_node
        self.add_to_head(new_node)

        if len(self.cache) > self.capacity:
            LRU = self.tail.prev
            self.remove(LRU)
            del self.cache[LRU.key]


