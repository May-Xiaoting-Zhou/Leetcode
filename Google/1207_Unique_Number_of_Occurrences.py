class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        set_cnt = set(cnt.values())
        return len(set_cnt) == len(cnt.values())

# Complexity Analysis
# Here, N is the size of array arr.

# Time complexity: O(N).

# We iterate over the array arr to find the frequency and store them in the hash map freq. Then, we insert these frequencies in the hash set freqSet, which has the insertion complexity of O(1). Hence, the total time complexity is equal to O(N).

# Space complexity: O(N).

# We are storing the N frequencies in the hash map freq that takes O(1) space for each element. We also store the frequency count in the hash set. Therefore, the total space complexity is equal to O(N).