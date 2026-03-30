class TimeMap:

    def __init__(self):

        self.key_value_store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:

        self.key_value_store[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:

        if key not in self.key_value_store:
            return ""
        
        max_seen_timestamp = 0
        max_seen_value = ''

        L = 0
        R = len(self.key_value_store[key]) - 1
        arr = self.key_value_store[key]
        result = ''

        while L <= R:

            mid = (L + R) // 2

            if arr[mid][1] <= timestamp:
                result = arr[mid][0]
                L = mid + 1
            
            else:
                R = mid - 1 
        
        return result



            