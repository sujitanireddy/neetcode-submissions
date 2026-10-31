class ListNode:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.value = value
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #Initializing doubly linked list 
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_at_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert_at_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self.insert_at_head(new_node)

        if len(self.cache) > self.capacity:
            LRU = self.tail.prev
            key = LRU.key
            self.remove(LRU)
            del self.cache[key]