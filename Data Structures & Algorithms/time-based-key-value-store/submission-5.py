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

        for value, ts in self.key_value_store[key]:

            if ts <= timestamp:

                max_seen_timestamp = max(max_seen_timestamp, ts)

                max_seen_value = value
        
        return max_seen_value
