class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]])

        return res

# Complexity Analysis
# Here n is the size of nums.

# Time complexity: O(n).

# At first glance, it may look like the time complexity of this algorithm should be O(n 
# 2
#  ), because there is a nested while loop inside the for loop. However, each element can only be added to the deque once, which means the deque is limited to n pushes. Every iteration of the while loop uses 1 pop, which means the while loop will not iterate more than n times in total, across all iterations of the for loop.
# An easier way to think about this is that in the worst case, every element will be pushed and popped once. This gives a time complexity of O(2⋅n)=O(n).
# Space complexity: O(k).

# The size of the deque can grow a maximum up to a size of k