class TimeMap:

    def __init__(self):
        self.key_value_store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        arr = self.key_value_store[key]
        L = 0
        R = len(arr) - 1
        value = ""

        while L <= R:

            mid = (L + R) // 2

            if arr[mid][1] <= timestamp:
                value = arr[mid][0]
                L = mid + 1
            
            else:
                R = mid - 1
        
        return value





        
