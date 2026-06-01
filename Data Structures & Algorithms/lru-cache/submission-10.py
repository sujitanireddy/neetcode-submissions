class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = ListNode(0,0)
        self.tail = ListNode(0,0) #LRU

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:

        if key in self.cache:
        
            node = self.cache[key]
            self.remove(node)
            self.add_to_head(node)

            return node.val
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:


        if key in self.cache:
            self.remove(self.cache[key])

        node = ListNode(key=key, val=value)
        self.add_to_head(node)
        self.cache[key] = node
        
        if self.capacity < len(self.cache):
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]



    