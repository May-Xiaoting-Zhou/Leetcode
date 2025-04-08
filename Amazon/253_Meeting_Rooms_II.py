class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals = sorted(intervals)
        # res = []
        # for inval in intervals:
        #     start, end = inval[0], inval[1]
        #     if len(res) == 0:
        #         res.append((start, end))
        #     else:
        #         FOUND = False
        #         for i in range(len(res) - 1, -1, -1):
        #             if res[i][1] <= start:
        #                 res[i] = (res[i][0], end)
        #                 FOUND = True
        #                 break
        #         if not FOUND:
        #             res.append((start, end))
        # return len(res)
        # if not intervals:
        #     return 0
        # free_rooms = []
        # intervals.sort(key = lambda x: x[0])
        # heapq.heappush(free_rooms, intervals[0][1])
        # for i in intervals[1:]:
        #     print(i, free_rooms)
        #     if free_rooms[0] <= i[0]:
        #         heapq.heappop(free_rooms)
        #     heapq.heappush(free_rooms, i[1])
        # return len(free_rooms)

        if not intervals:
            return 0
        used_rooms = 0
        start_timings = sorted(i[0] for i in intervals)
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        end_pointer, start_pointer = 0, 0
        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            used_rooms += 1
            start_pointer += 1
        return used_rooms

# Complexity Analysis

# Time Complexity: O(NlogN) because all we are doing is sorting the two arrays for start timings and end timings individually and each of them would contain N elements considering there are N intervals.

# Space Complexity: O(N) because we create two separate arrays of size N, one for recording the start times and one for the end times.