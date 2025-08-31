class TimeMap:
 """
    Time-based key-value store.

    Internally uses a dictionary:
        key -> list of (timestamp, value) pairs (sorted by timestamp)

    Example:
        After the following operations:
            set("foo", "bar", 1)
            set("foo", "baz", 4)

        The internal map looks like:
            {
                "foo": [(1, "bar"), (4, "baz")]
            }

    Why not timestamp -> {key:value}?
        - If you store data like {1: {"foo":"bar"}, 4: {"foo":"baz"}},
          then looking up get("foo", 3) requires searching ALL timestamps
          and checking if "foo" exists there.
        - That leads to inefficiency and potential errors when a key is
          missing at some timestamps.
        - By grouping by key, each key has its own timeline, and we only
          binary search within its history.
"""
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            mp_list = self.map[key]
            l = 0
            r = len(mp_list) - 1
            answer = ""
            while l <= r:
                mid = l + (r - l) // 2
                if mp_list[mid][0] <= timestamp:
                    answer = mp_list[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
            return answer 

        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)