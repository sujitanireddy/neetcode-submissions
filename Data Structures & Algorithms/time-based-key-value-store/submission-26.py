"""
Notes:

{                   L
                M
                R
    alice : [(1,happy)]
}

In the get operation: if a val does not exisit, return the next smallest

{
    alice : [(happy,1),(sad,3)]
}

O(log n)        
                      M
                      L R
                  0 1 2 3
                  4 5 7 8
                
while L <= R:
if  val[mid] > target:
    R = mid - 1
else
    ans = record the value at mid
    L = mid + 1

ans = 5
"""
class TimeMap:

    def __init__(self):
        self.key_value_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        arr = self.key_value_store[key]

        L = 0
        R = len(arr) - 1

        while L <= R:

            mid = (L + R) // 2

            if arr[mid][0] > timestamp:

                R = mid - 1
            
            else:

                res = arr[mid][1]

                L = mid + 1

        return res

        
        
