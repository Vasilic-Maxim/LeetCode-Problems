from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(log (n)) or O(n)
    """

    def pathSum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        paths = []

        def traverse(node: TreeNode, path: List[int]):
            if node is None:
                return

            path.append(node.val)

            if node.left is None and node.right is None:
                if sum(path) == target_sum:
                    paths.append(path[:])
            else:
                traverse(node.left, path)
                traverse(node.right, path)

            path.pop()

        traverse(root, [])
        return paths
