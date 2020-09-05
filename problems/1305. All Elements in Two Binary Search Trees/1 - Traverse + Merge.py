from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time/Space: O(m + n)
    """

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        path1 = self.traverse(root1)
        path2 = self.traverse(root2)
        return self.merge(path1, path2)

    def merge(self, path1: List[int], path2: List[int]) -> List[int]:
        l1, l2 = len(path1), len(path2)
        p1 = p2 = 0
        result = []
        while p1 < l1 and p2 < l2:
            if path1[p1] < path2[p2]:
                result.append(path1[p1])
                p1 += 1
            else:
                result.append(path2[p2])
                p2 += 1

        if p1 < l1:
            result.extend(path1[p1:])
        if p2 < l2:
            result.extend(path2[p2:])

        return result

    def traverse(self, node: TreeNode) -> List[int]:
        path1 = []
        self.dfs(node, path1)
        return path1

    def dfs(self, node: TreeNode, path: List[int]):
        if node is None:
            return

        self.dfs(node.left, path)
        path.append(node.val)
        self.dfs(node.right, path)
