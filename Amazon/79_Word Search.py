class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # if len(word) > len(board) * len(board[0]):
        #     return False

        # while len(board[0]) > 1 and len(word) > len(board[0]) and len(set(word[:len(board[0])])) == 1 and word[:len(board[0])] == ''.join(board[0]):
        #     word = word[len(board[0]):]
        #     board = board[1:]
            
        #     if len(board) == 1:
        #         return word == ''.join(board[0])

        # letter_position = collections.defaultdict(list)
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         letter_position[board[i][j]].append((i, j))
        
        # # Approach: BFS (deque)
        # idx = 0
        # dq = deque()
        # for pos in letter_position[word[idx]]:
        #     dq.append([pos])
        # DEAD_END = []
        
        # while dq:
        #     nodes = dq.popleft()
        #     idx = len(nodes) - 1
        #     if idx == len(word) - 1:
        #         return True
        #     else:
        #         node = nodes[-1]
                
        #         left = (node[0], max((node[1] - 1), 0))
        #         right = (node[0], min(node[1] + 1, len(board[0]) - 1))
        #         bottom = (min(node[0] + 1, len(board) - 1), node[1])
        #         top = (max((node[0] - 1), 0), node[1])

        #         if word[idx+1] not in letter_position:
        #             return False
                
        #         for pos in letter_position[word[idx+1]]:
        #             _nodes = nodes.copy()
        #             if pos == left and left not in _nodes:
        #                 _nodes.append(left)
        #                 dq.append(_nodes)
        #             if pos == right and right not in _nodes:
        #                 _nodes.append(right)
        #                 dq.append(_nodes)
        #             if pos == bottom and bottom not in _nodes:
        #                 _nodes.append(bottom)
        #                 dq.append(_nodes)
        #             if pos == top and top not in _nodes:
        #                 _nodes.append(top)
        #                 dq.append(_nodes)
                    
        # return False
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row: int, col: int, suffix: str) -> bool:
        if len(suffix) == 0:
            return True

        if (
            row < 0
            or row == self.ROWS
            or col < 0
            or col == self.COLS
            or self.board[row][col] != suffix[0]
        ):
            return False
        
        self.board[row][col] = "#"
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True
        self.board[row][col] = suffix[0]
        return False

# Complexity Analysis
# Time Complexity: O(N⋅3 
# L
#  ) where N is the number of cells in the board and L is the length of the word to be matched.

# For the backtracking function, initially we could have at most 4 directions to explore, but further the choices are reduced into 3 (since we won't go back to where we come from).
# As a result, the execution trace after the first step could be visualized as a 3-nary tree, each of the branches represent a potential exploration in the corresponding direction. Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 3-nary tree, which is about 3 
# L
#  .

# We iterate through the board for backtracking, i.e. there could be N times invocation for the backtracking function in the worst case.

# As a result, overall the time complexity of the algorithm would be O(N⋅3 
# L
#  ).

# Space Complexity: O(L) where L is the length of the word to be matched.

# The main consumption of the memory lies in the recursion call of the backtracking function. The maximum length of the call stack would be the length of the word. Therefore, the space complexity of the algorithm is O(L).