class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        # DFS
        # def dfs(land, grid) -> int:
        #     x, y = land[0], land[1]
        #     if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):
        #         if grid[x][y] == "0":
        #             return 0
        #         else:
        #             grid[x][y] = "0"
        #             # left
        #             if x - 1 >= 0:
        #                 dfs((x - 1, y), grid)
        #             # right
        #             if x + 1 <= len(grid) - 1:
        #                 dfs((x + 1, y), grid)
        #             # up
        #             if y - 1 >= 0:
        #                 dfs((x, y - 1), grid)
        #             # down
        #             if y + 1 <= len(grid[0]) - 1:
        #                 dfs((x, y + 1), grid)
        #             return 1
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == "1":
        #             cnt += dfs((i, j), grid)
        # return cnt
        # BFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    grid[i][j] = 0
                    neighbor = collections.deque([(i, j)])
                    while neighbor:
                        x0, y0 = neighbor.popleft()
                        for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            x = x0 + move[0]
                            y = y0 + move[1]
                            if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == "1":
                                neighbor.append((x, y))
                                grid[x][y] = "0"
                    
        return cnt


# DFS
# Complexity Analysis

# Time complexity : O(M×N) where M is the number of rows and
# N is the number of columns.

# Space complexity : worst case O(M×N) in case that the grid map
# is filled with lands where DFS goes by M×N deep.

# BFS
# Complexity Analysis

# Time complexity : O(M×N) where M is the number of rows and
# N is the number of columns.

# Space complexity : O(min(M,N)) because in worst case where the
# grid is filled with lands, the size of queue can grow up to min(M,N).