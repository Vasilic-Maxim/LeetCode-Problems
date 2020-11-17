from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        Workflow:
        - find the path to the target node in the original tree
        - use that path to find the same node in cloned tree

        Complexity:
        Time: O(n)
        Space: O(p)

        Where:
        n = number of nodes in original tree
        p = length of the path in the tree to the target-node
        """

        path = []
        self.find_path(original, target, path, 0)
        return self.get(cloned, path)

    def find_path(self, node: TreeNode, target: TreeNode, path: List[int], direction: int) -> bool:
        if node is not None:
            path.append(direction)

            if (node is target or
                    self.find_path(node.left, target, path, 0) or
                    self.find_path(node.right, target, path, 1)):
                return True

            path.pop()

        return False

    def get(self, root: TreeNode, path: List[int]):
        for i in range(1, len(path)):
            root = root.right if path[i] else root.left

        return root
