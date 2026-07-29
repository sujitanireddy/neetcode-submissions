class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict()
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.delete(node)
        self.insert_at_head(node)

        return node.val
    
    def delete(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.delete(self.cache[key])

        node = ListNode(key, value)
        self.cache[key] = node
        self.insert_at_head(node)

        while len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.delete(lru)
            print(lru.key)
            print(self.cache)
            del self.cache[lru.key]
        







