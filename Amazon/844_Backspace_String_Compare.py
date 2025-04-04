class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspaceStr(stack, st):
            for c in st:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        stack_1, stack_2 = backspaceStr([], s), backspaceStr([], t)
        return stack_1 == stack_2

# Complexity Analysis

# Time Complexity: O(M+N), where M,N are the lengths of S and T respectively.

# Space Complexity: O(M+N).