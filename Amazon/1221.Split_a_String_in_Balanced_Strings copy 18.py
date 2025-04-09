class Solution: 
    class Course:
        def __init__(self, val):
            self.val = val
            self.next = [] 
    
    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        
        visit[node] = True
        inStack[node] = True

        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True

        inStack[node] = False
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        visit = [False] * numCourses
        inStack = [False] * numCourses

        for i in range(numCourses):
            if self.dfs(i, adj, visit, inStack):
                return False

        return True

        # lst = [self.Course(i) for i in range(numCourses)]
        # for pre in prerequisites:
        #     lst[pre[1]].next.append(lst[pre[0]])

        # courses_links = []
        # for i in range(numCourses): 
        #     root = lst[i]
        #     link = []
        #     while root:
        #         if root.val in link:
        #             return False
    
        #         link.append(root.val)
        #         if root.next:
        #             root = root.next.pop()
        #         else:
        #             break

        #     courses_links.append(link)

        # for j in range(numCourses):
        #     for n in courses_links[j][:-1]:
        #         if n in courses_links[courses_links[j][-1]]:
        #             return False
        
        # return True
        # indegree = [0] * numCourses
        # adj = [[] for _ in range(numCourses)]

        # for prerequisite in prerequisites:
        #     adj[prerequisite[1]].append(prerequisite[0])
        #     indegree[prerequisite[0]] += 1
        
        # queue = deque()
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         queue.append(i)

        # nodesVisited = 0
        # while queue:
        #     node = queue.popleft()
        #     nodesVisited += 1

        #     for neighbor in adj[node]:
        #         indegree[neighbor] -= 1

        #         if indegree[neighbor] == 0:
        #             queue.append(neighbor)
        # return nodesVisited == numCourses

# Complexity Analysis
# Here, n be the number of courses and m be the size of prerequisites.

# Time complexity: O(m+n)

# Initializing the adj list takes O(m) time as we go through all the edges. The indegree array take O(n) time.
# Each queue operation takes O(1) time, and a single node will be pushed once, leading to O(n) operations for n nodes. We iterate over the neighbors of each node that is popped out of the queue iterating over all the edges once. Since there are total of m edges, it would take O(m) time to iterate over the edges.
# Space complexity: O(m+n)

# The adj arrays takes O(m) space. The indegree array takes O(n) space.
# The queue can have no more than n elements in the worst-case scenario. It would take up O(n) space in that case.