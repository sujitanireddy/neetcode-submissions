"""
- Added key-value pair on to the cache
- Size of the cache should always be within capacity. If capacity is exceeded remove LRU

DS used:
- Hashmap {key : value}
- doubly linked list

{
 1: 10
 2: 20
}

LRU   listNode(1,10)  listNode(2,10)    MRU

ListNode()
key
value
next
prev

{
 1: ListNode(1,10)
 
}

head <-> ListNode(2:20) <-> ListNode(1:10) <-> tail
"""

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict()
        self.capacity = capacity
        
        self.head = ListNode(0,0) #MRU
        self.tail = ListNode(0,0) #LRU

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove_node(node)
        self.insert_at_head(node)
        
        return node.value


    def insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove_node(self.cache[key])
        
        self.cache[key] = ListNode(key, value)

        node = self.cache[key]
        self.insert_at_head(node)

        while self.capacity < len(self.cache):
            LRU = self.tail.prev
            self.remove_node(LRU)

            del self.cache[LRU.key]






        
