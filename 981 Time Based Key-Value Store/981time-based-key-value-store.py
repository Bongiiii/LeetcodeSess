from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        #dictionary to store key-value pairs
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #store the key value pairs in hashset
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Base case: key not found
        if key not in self.store:
            return ""

        pair = self.store[key]
        # Find the index where timestamp would be inserted
        i = bisect_right(pair, (timestamp, ""))

        # If i == 0, it means there is no valid timestamp <= given timestamp
        if i == 0:
            return "" 
        
        # Otherwise, return the value at the largest valid timestamp
        return pair[i - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)