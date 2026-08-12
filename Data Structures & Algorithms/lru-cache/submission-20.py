"""
MRU (head) <-> (tail) LRU

(3:30) (2,20) (1,10)
{
    1 : (1,10)
}

GET:
- detach the list node
- attach to head
- return value

PUT:
- If we are updating an exisiting node, remove the old node and add new one

- Create a list node
- Add the key : Listnode to hashmap
- attach to head

    if size >= cache capacity: remove LRU (node attached to tail)
        - delete from hashmap

      (2,20)

      (3,35)

(head) <->  (2,20) <-> (tail) 

"""
class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict()

        #head <-> tail
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def detach(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        
    def attach_to_head(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.detach(node)
        self.attach_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.detach(self.cache[key])

        node = ListNode(key,value)
        self.cache[key] = node
        self.attach_to_head(node)

        if len(self.cache) > self.capacity:
            LRU = self.tail.prev
            self.detach(LRU)
            del self.cache[LRU.key]


        
