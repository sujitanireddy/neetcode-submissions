class TimeMap:

    def __init__(self):
        self.keystore = collections.defaultdict(list)
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keystore:
            return ""
    
        else:
            seen = 0
            seen_value = ''
            for value_time in self.keystore[key]:
                if value_time[1] <= timestamp:
                    seen = max(seen, value_time[1])
                    seen_value = value_time[0]
            
        return seen_value
        
