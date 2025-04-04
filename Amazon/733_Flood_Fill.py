class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image

# Complexity Analysis

# Time Complexity: O(N), where N is the number of pixels in the image. We might process every pixel.

# Space Complexity: O(N), the size of the implicit call stack when calling dfs.