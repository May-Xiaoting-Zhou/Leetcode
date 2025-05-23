class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result

# Complexity Analysis

# Let M be the number of rows and N be the number of columns.

# Time complexity: O(M⋅N). This is because we visit each element once.

# Space complexity: O(1). This is because we don't use other data structures. Remember that we don't include the output array in the space complexity.

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         VISITED = 101
#         rows, columns = len(matrix), len(matrix[0])
#         # Four directions that we will move: right, down, left, up.
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         # Initial direction: moving right.
#         current_direction = 0
#         # The number of times we change the direction.
#         change_direction = 0
#         # Current place that we are at is (row, col).
#         # row is the row index; col is the column index.
#         row = col = 0
#         # Store the first element and mark it as visited.
#         result = [matrix[0][0]]
#         matrix[0][0] = VISITED

#         while change_direction < 2:

#             while True:
#                 # Calculate the next place that we will move to.
#                 next_row = row + directions[current_direction][0]
#                 next_col = col + directions[current_direction][1]

#                 # Break if the next step is out of bounds.
#                 if not (0 <= next_row < rows and 0 <= next_col < columns):
#                     break
#                 # Break if the next step is on a visited cell.
#                 if matrix[next_row][next_col] == VISITED:
#                     break

#                 # Reset this to 0 since we did not break and change the direction.
#                 change_direction = 0
#                 # Update our current position to the next step.
#                 row, col = next_row, next_col
#                 result.append(matrix[row][col])
#                 matrix[row][col] = VISITED

#             # Change our direction.
#             current_direction = (current_direction + 1) % 4
#             # Increment change_direction because we changed our direction.
#             change_direction += 1

#         return result

# Complexity Analysis

# Let M be the number of rows and N be the number of columns.

# Time complexity: O(M⋅N). This is because we visit each element once.

# Space complexity: O(1). This is because we don't use other data structures. Remember that we don't consider the output array or the input matrix when calculating the space complexity. However, if we were prohibited from mutating the input matrix, then this would be an O(M⋅N) space solution. This is because we would need to use a boolean matrix to track all of the previously seen cells.