from bisect import bisect_right

class TimeMap:

    def __init__(self):
        #hashmap with tuple that stores key - value((timestamp, value)) pair
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #adding to hashmap
        self.hashMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #base case key doesnt exist in hashmap
        if key not in self.hashMap:
            return ""

        #use binary search logic as timestamp is in increasing order
        #implement with bisectright
        time_value = self.hashMap[key]
        elem = bisect_right(time_value, (timestamp, chr(127)))

        return time_value[elem-1][1] if elem else "" 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)