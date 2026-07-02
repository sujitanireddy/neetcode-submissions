class TimeMap:

    """
    time_store = defaultdict(list) { alice: [(happy, 1), (sad, 3)]}
                 
             
              L
              R    
            1 3 5 6 7
        
    """

    def __init__(self):
        self.key_value_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        arr = self.key_value_store[key]

        #binary search

        L = 0
        R = len(arr) - 1
        output = ""

        while L <= R:

            mid = (L + R) // 2

            if arr[mid][1] <= timestamp:
                output = arr[mid][0]
                L = mid + 1
            
            elif arr[mid][1] > timestamp:
                R = mid - 1
        
        return output














       

