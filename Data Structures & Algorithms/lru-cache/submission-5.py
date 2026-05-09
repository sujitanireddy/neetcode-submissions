class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def remove_node(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        
    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove_node(node)
        self.add_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove_node(self.cache[key])
        
        node = ListNode(key, value)
        self.cache[key] = node
        self.add_to_head(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove_node(lru)
            del self.cache[lru.key]


        

        

