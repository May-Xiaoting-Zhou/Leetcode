class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def runRotteingProcess(timestamp):
            TBC = False
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == timestamp:
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    grid[n_row][n_col] = timestamp + 1
                                    TBC = True
            return TBC
        timestamp = 2
        while runRotteingProcess(timestamp):
            timestamp += 1

        for row in grid:
            for cell in row:
                if cell == 1:
                    return -1

        return timestamp - 2
        # def rotting(start, grid):
        #     i, j, step = start

        #     l = (i, max(0, j - 1), step + 1)
        #     r = (i, min(j + 1, len(grid[0]) - 1), step + 1)
        #     u = (max(0, i - 1), j, step + 1)
        #     d= (min(i + 1, len(grid) - 1), j, step + 1)
            
        #     if grid[l[0]][l[1]] == 1 or (grid[l[0]][l[1]] >= 3 and grid[l[0]][l[1]] > l[2]):
        #         grid[l[0]][l[1]] = l[2]
        #         rotting(l, grid)

        #     if grid[r[0]][r[1]] == 1 or (grid[r[0]][r[1]] >= 3 and grid[r[0]][r[1]] > r[2]):
        #         grid[r[0]][r[1]] = r[2]
        #         rotting(r, grid)

        #     if grid[u[0]][u[1]] == 1 or (grid[u[0]][u[1]] >= 3 and grid[u[0]][u[1]] > u[2]):
        #         grid[u[0]][u[1]] = u[2]
        #         rotting(u, grid)

        #     if grid[d[0]][d[1]] == 1 or (grid[d[0]][d[1]] >= 3 and grid[d[0]][d[1]] > d[2]):
        #         grid[d[0]][d[1]] = d[2]
        #         rotting(d, grid)
        
        # self.max_min = 2
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])): 
        #         if grid[i][j] == 2:
        #             start = (i, j, 2)
        #             rotting(start, grid)
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             return -1
        #         self.max_min = max(self.max_min, grid[i][j])
        
        # return self.max_min - 2
# Complexity Analysis
# Time Complexity: O(N 
# 2
#  M 
# 2
#  ) where N×M is the size of the input grid.


# In the in-place BFS traversal, for each round of BFS, we would have to iterate through the entire grid.


# The contamination propagates in 4 different directions. If the orange is well adjacent to each other, the chain of propagation would continue until all the oranges turn rotten.


# In the worst case, the rotten and the fresh oranges might be arranged in a way that we would have to run the BFS loop over and over again, which could amount to  
# 2
# NM
# ​
#   times which is the longest propagation chain that we might have, i.e. the zigzag walk in a 2D grid as shown in the following graph.
# Grid Zigzag


# As a result, the overall time complexity of the in-place BFS algorithm is O(NM⋅ 
# 2
# NM
# ​
#  )=O(N 
# 2
#  M 
# 2
#  ).

# Space Complexity: O(1), the memory usage is constant regardless the size of the input. This is the very point of applying in-place algorithm. Here we trade the time complexity with the space complexity, which is a common scenario in many algorithms.