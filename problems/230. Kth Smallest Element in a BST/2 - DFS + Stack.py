class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Note:
    You pay "k" for "pop"-ing elements from the stack

    ====== Unbalanced Tree (all nodes on the left side) =====
    Time: O(n + k)
    Space: O(n)

    ====== Balanced Tree =====
    Time: O(log (n) + k)
    Space: O(n)
    """

    def kthSmallest(self, node: TreeNode, k: int) -> int:
        stack = []
        while 1:
            # rich left most point
            while node is not None:
                stack.append(node)
                node = node.left
            # take last valid node from stack
            node = stack.pop()
            # check if we are at the right place
            k -= 1
            if not k:
                return node.val
            # go right
            node = node.right
