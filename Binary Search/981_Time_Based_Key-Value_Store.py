import collections
import bisect

class TimeMap:
    def __init__(self):
        self.timeMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap or not self.timeMap[key]:
            return ""

        timestamps = self.timeMap[key]
        idx = bisect.bisect_right(timestamps, (timestamp, chr(127))) - 1  # Binary search

        return timestamps[idx][1] if idx >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Time Complexity Analysis

# 1. Initialization (__init__ method)
# 	•	self.timeMap = collections.defaultdict(list): Initializes an empty dictionary.
# 	•	Time Complexity:  O(1) 

# 2. Storing a Key-Value Pair (set method)
# 	•	self.timeMap[key].append((timestamp, value)):
# 	•	Appending an element to a list is an  O(1)  operation.
# 	•	Time Complexity:  O(1) 

# 3. Retrieving a Value (get method)
# 	•	Uses binary search (bisect_right), which takes  O(\log n) , where  n  is the number of timestamps stored for the given key.
# 	•	Time Complexity:  O(\log n) 

# Space Complexity Analysis

# 1. Initialization (__init__ method)
# 	•	A dictionary is initialized, but it’s empty at the start.
# 	•	Space Complexity:  O(1) 

# 2. Storing a Key-Value Pair (set method)
# 	•	Every call to set stores a new (timestamp, value) tuple.
# 	•	In the worst case, for  m  unique keys with  n  timestamps each, we store  O(mn)  elements.
# 	•	Space Complexity:  O(mn) 

# 3. Retrieving a Value (get method)
# 	•	Only a few variables (idx, timestamps) are used.
# 	•	Space Complexity:  O(1) 