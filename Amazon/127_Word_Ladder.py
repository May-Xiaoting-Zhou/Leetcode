from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.lengh: int = 0
        self.all_combo_dict: Dict[str, List[str]] = defaultdict(list)

    def visitWordNode(
        self, queue: Deque[str], visited: Dict[str, int], others_visited: Dict[str, int]
    ) -> Any:
        queue_size: int = len(queue)
        for _ in range(queue_size):
            current_word: str = queue.popleft()
            for i in range(self.length):
                intermediate_word: str = current_word[:i] + "*" + current_word[i + 1 :]
                for word in self.all_combo_dict[intermediate_word]:
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        visited[word] = visited[current_word] + 1
                        queue.append(word)

        return None

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        self.length = len(beginWord)

        # L = len(beginWord)
        # all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        queue_begin: Deque[str] = deque([beginWord])
        queue_end: Deque[str] = deque([endWord])

        visited_begin: Dict[str, int] = {beginWord: 1}
        visited_end: Dict[str, int] = {endWord: 1}
        ans: Any = None
        while queue_begin and queue_end:
            if len(queue_begin) <= len(queue_end):
                ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            else:
                ans = self.visitWordNode(queue_end, visited_end, visited_begin)

            if ans:
                return ans

        # queue = deque([(beginWord, 1)])
        # visited = {beginWord: True}

        # while queue:
        #     current_word, level = queue.popleft()
        #     for i in range(L):
        #         intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
        #         for word in all_combo_dict[intermediate_word]:
        #             if word == endWord:
        #                 return level + 1
        #             if word not in visited:
        #                 visited[word] = True
        #                 queue.append((word, level + 1))
        #     all_combo_dict[intermediate_word] = []

        return 0

# Approach 1: Breadth First Search
# Intuition

# Start from beginWord and search the endWord using BFS.
# Complexity Analysis

# Time Complexity: O(M 
# 2
#  ×N), where M is the length of each word and N is the total number of words in the input word list.

# For each word in the word list, we iterate over its length to find all the intermediate words corresponding to it. Since the length of each word is M and we have N words, the total number of iterations the algorithm takes to create all_combo_dict is M×N. Additionally, forming each of the intermediate word takes O(M) time because of the substring operation used to create the new string. This adds up to a complexity of O(M 
# 2
#  ×N).

# Breadth first search in the worst case might go to each of the N words. For each word, we need to examine M possible intermediate words/combinations. Notice, we have used the substring operation to find each of the combination. Thus, M combinations take O(M 
# 2
#  ) time. As a result, the time complexity of BFS traversal would also be O(M 
# 2
#  ×N).

# Combining the above steps, the overall time complexity of this approach is O(M 
# 2
#  ×N).

# Space Complexity: O(M 
# 2
#  ×N).

# Each word in the word list would have M intermediate combinations. To create the all_combo_dict dictionary we save an intermediate word as the key and its corresponding original words as the value. Note, for each of M intermediate words we save the original word of length M. This simply means, for every word we would need a space of M 
# 2
#   to save all the transformations corresponding to it. Thus, all_combo_dict would need a total space of O(M 
# 2
#  ×N).
# Visited dictionary would need a space of O(M×N) as each word is of length M.
# Queue for BFS in worst case would need a space for all O(N) words and this would also result in a space complexity of O(M×N).
# Combining the above steps, the overall space complexity is O(M 
# 2
#  ×N) + O(M∗N) + O(M∗N) = O(M 
# 2
#  ×N) space.

#  Approach 2: Bidirectional Breadth First Search
# Intuition

# The graph formed from the nodes in the dictionary might be too big. The search space considered by the breadth first search algorithm depends upon the branching factor of the nodes at each level. If the branching factor remains the same for all the nodes, the search space increases exponentially along with the number of levels. Consider a simple example of a binary tree. With each passing level in a complete binary tree, the number of nodes increase in powers of 2.


# Complexity Analysis

# Time Complexity: O(M 
# 2
#  ×N), where M is the length of words and N is the total number of words in the input word list. Similar to one directional, bidirectional also takes O(M 
# 2
#  ×N) time for finding out all the transformations. But the search time reduces to half, since the two parallel searches meet somewhere in the middle.

# Space Complexity: O(M 
# 2
#  ×N), to store all M transformations for each of the N words in the all_combo_dict dictionary, same as one directional. But bidirectional reduces the search space. It narrows down because of meeting in the middle.