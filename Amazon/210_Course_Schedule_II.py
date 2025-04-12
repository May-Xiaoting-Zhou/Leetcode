class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # inDegrees = [0] * numCourses
        # neighbors = [[] for i in range(numCourses)]
        # dq = deque()
        # for pre in prerequisites:
        #     inDegrees[pre[0]] += 1
        #     neighbors[pre[1]].append(pre[0])
        
        # for n in range(numCourses):
        #     if inDegrees[n] == 0:
        #         dq.append(n)
        
        # res = []
        # while dq:
        #     numCourse = dq.popleft() 
        #     res.append(numCourse)

        #     for neighbor in neighbors[numCourse]:
        #         inDegrees[neighbor] -= 1
        #         if inDegrees[neighbor] == 0:
        #             dq.append(neighbor)
        
        # return res if len(res) == numCourses else []
        # DFS
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        topological_sorted_order = []
        is_possible = True

        color = {k: Solution.WHITE for k in range(numCourses)}
        
        def dfs(node: int) -> None:
            nonlocal is_possible
            if not is_possible:
                return
            color[node] = Solution.GRAY

            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        is_possible = False # circle
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)
        
        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
        return topological_sorted_order[::-1] if is_possible else []

            
# Complexity Analysis
# Time Complexity: O(V+E) where V represents the number of vertices and E represents the number of edges.
# Essentially we iterate through each node and each vertex in the graph once and only once.

# Space Complexity: O(V+E).

# We use the adjacency list to represent our graph initially. The space occupied is defined by the number of edges because for each node as the key, we have all its adjacent nodes in the form of a list as the value. Hence, O(E)

# Additionally, we apply recursion in our algorithm, which in worst case will incur O(E) extra space in the function call stack.

# To sum up, the overall space complexity is O(V+E).