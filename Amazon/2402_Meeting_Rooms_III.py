class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # room_availability_time = [0] * n
        # meeting_count = [0] * n
        # for start, end in sorted(meetings):
        #     min_room_availability_time = inf
        #     min_availability_romm = 0
        #     found_unused_room = False
        #     for i in range(n):
        #         if room_availability_time[i] <= start:
        #             found_unused_room = True
        #             meeting_count[i] += 1
        #             room_availability_time[i] = end
        #             break
        #         if min_room_availability_time > room_availability_time[i]:
        #             min_room_availability_time = room_availability_time[i]
        #             min_available_time_room = i
        #     if not found_unused_room:
        #         room_availability_time[min_available_time_room] += end - start
        #         meeting_count[min_available_time_room] += 1
        # return meeting_count.index(max(meeting_count))
        unused_rooms, used_rooms = list(range(n)), []
        heapify(unused_rooms)
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)

            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, [end, room])
            else:
                room_availability_time, room = heappop(used_rooms)
                heappush(
                    used_rooms,
                    [room_availability_time + end - start, room]
                )
            meeting_count[room] += 1
        return meeting_count.index(max(meeting_count))
                
# Complexity Analysis
# Let N be the number of rooms.
# Let M be the number of meetings.

# Time complexity: O(M⋅logM+M⋅logN). Sorting meetings will incur a time complexity of O(M⋅logM). Popping and pushing into the priority queue will each cost O(logN). These priority queue operations run inside a for loop that runs at most M times leading to a time complexity of O(M⋅logN).
# The inner nested loop will incur a time complexity of O(logN). The combined time complexity will be O(M⋅logM+M⋅logN). As per the constraints N is small, the term O(M⋅logM) will dominate.
# Note: Initializing unused_rooms will cost O(N) in ruby and python. But will cost O(N⋅logN) in C++ and Java due to the implementation.

# Space complexity: O(N+sort). Initializing unused_rooms and meeting_count will incur a space complexity of O(N). Some extra space is used when we sort an array of size N in place. The space complexity of the sorting algorithm depends on the programming language.

# In Python, the sort method sorts a list using the Timsort algorithm which is a combination of Merge Sort and Insertion Sort and has a space complexity of O(N).
# In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worst-case space complexity of O(logN).
# In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of O(logN).