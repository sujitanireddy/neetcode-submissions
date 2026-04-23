class Node:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node

        self.head = Node() #MRU
        self.tail = Node() #LRU
        self.head.next = self.tail
        self.tail.prev = self.head

    #helper function to remove a node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    #helper funtion to insert a node right after head (MRU)
    def insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert_at_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert_at_head(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
        
