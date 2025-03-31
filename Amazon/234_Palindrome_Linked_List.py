class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

# Complexity Analysis

# Time complexity : O(n), where n is the number of nodes in the Linked List.

# In the first part, we're copying a Linked List into an Array List. Iterating down a Linked List in sequential order is O(n), and each of the n writes to the ArrayList is O(1). Therefore, the overall cost is O(n).

# In the second part, we're using the two pointer technique to check whether or not the Array List is a palindrome. Each of the n values in the Array list is accessed once, and a total of O(n/2) comparisons are done. Therefore, the overall cost is O(n). The Python trick (reverse and list comparison as a one liner) is also O(n).

# This gives O(2n)=O(n) because we always drop the constants.

# Space complexity : O(n), where n is the number of nodes in the Linked List.

# We are making an Array List and adding n values to it.