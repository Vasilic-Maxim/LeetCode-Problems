from typing import List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space (unbalanced tree): O(n)
    Space (balanced tree): O(log (n))
    """

    def sumNumbers(self, root: TreeNode) -> int:
        stack: List[Tuple[TreeNode, int]] = [(root, 0)]
        result = 0
        while stack:
            node, path = stack.pop()

            if node is not None:
                path = path * 10 + node.val

                if node.left is None and node.right is None:
                    result += path
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))

        return result
