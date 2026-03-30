class TimeMap:

    def __init__(self):
        self.keystore = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keystore:
            return ""
    
        else:
            l = 0
            r = len(self.keystore[key]) - 1
            result = ""

            while l <= r:

                mid = (l+r) // 2
                
                if self.keystore[key][mid][1] <= timestamp:
                    result = self.keystore[key][mid][0]
                    l = mid + 1
                
                else:

                    r = mid - 1
            
            return result