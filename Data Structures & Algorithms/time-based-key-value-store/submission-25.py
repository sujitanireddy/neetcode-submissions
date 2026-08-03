"""
{
 alice: (1, happy)
 alice: (3, sad)
 bob : (1,mad), (2,dad), (3,cad)
   
           
L  M  R
1, 2, 3

L > R!

mid > ts: 
    keep track of the word
    R = mid - 1
}
For get method
- If the given timestamp is < the timestamps exisiting then we just return the value which is smaller, if not ts exists which is smaller 
we just return ""
"""
class TimeMap:

    def __init__(self):
        self.key_value_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.key_value_store:
            return ""

        arr = self.key_value_store[key]
        res = ""

        L = 0
        R = len(arr) - 1

                         
            #L           M         R         
        #[(1, happy), (2,sad), (3,mad)]

        while L <= R:

            mid = (L+R) // 2

            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                L = mid + 1
            
            else:
                R = mid - 1 
        
        return res
        


