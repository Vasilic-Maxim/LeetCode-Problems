class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    n - total number of nodes need to be traversed
    Time: O(n)
    Space: O(n)
    """

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        stack = [t1, t2]
        while stack and stack:
            node2 = stack.pop()
            node1 = stack.pop()

            if node1 is not None and node2 is not None:
                node1.val += node2.val

                if node1.left is not None:
                    stack.extend([node1.left, node2.left])
                else:
                    node1.left = node2.left

                if node1.right is not None:
                    stack.extend([node1.right, node2.right])
                else:
                    node1.right = node2.right
        return t1
