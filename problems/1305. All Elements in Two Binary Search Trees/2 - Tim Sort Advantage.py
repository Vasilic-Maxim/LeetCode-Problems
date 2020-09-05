from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Before you scream "But sorting isn't linear!",
    know that it's →Timsort, which identifies the
    two already sorted runs as such and simply
    merges them. And since it's done in C, it's
    likely faster than if I tried merging myself
    in Python. (c)StefanPochmann

    n - total number of elements in both trees
    Time/Space: O(n)
    """

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        self.traverse(root1, result)
        self.traverse(root2, result)
        return sorted(result)

    def traverse(self, node: TreeNode, path: List[int]):
        if node is not None:
            self.traverse(node.left, path)
            path.append(node.val)
            self.traverse(node.right, path)
