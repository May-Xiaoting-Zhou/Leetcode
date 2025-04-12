class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [n * -1 for n in nums]
        # heapq.heapify(nums)
        # res = -1
        # for i in range(k):
        #     res = heapq.heappop(nums)
        # return -res

        # Approach: Quickselect
        # def quick_select(nums, k):
        #     pivot = random.choice(nums)
        #     left, right, mid = [], [], []
        #     for num in nums:
        #         if num > pivot:
        #             left.append(num)
        #         elif num < pivot:
        #             right.append(num)
        #         else:
        #             mid.append(num)
            
        #     if k <= len(left):
        #         return quick_select(left, k)
        #     if k > len(left) + len(mid):
        #         return quick_select(right, k - (len(left) + len(mid)))
            
        #     return pivot

        # return quick_select(nums, k)

        # Approach: Counting Sort
        min_val, max_val = min(nums), max(nums)
        count = [0] * (max_val - min_val + 1)
        for n in nums:
            count[n - min_val] += 1
        
        sum_cnt = 0
        for i in range(len(count) - 1, -1, -1):
            sum_cnt += count[i]
            if sum_cnt >= k:
                return i + min_val
        return -1

# Approach: Quickselect
Time complexity: O(n) on average, O(n ** 2) in the worst case
Space complexity: O(n)

# Approach: Counting Sort
# Complexity Analysis

# Given n as the length of nums and m as maxValue - minValue, Time complexity: O(n+m)

# We first find maxValue and minValue, which costs O(n).
# Next, we initialize count, which costs O(m).
# Next, we populate count, which costs O(n).
# Finally, we iterate over the indices of count, which costs up to O(m).

# Space complexity: O(m), We create an array count with size O(m).