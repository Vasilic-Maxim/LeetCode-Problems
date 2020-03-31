class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    n - number of elements in tree
    Time: O(n)
    Space: O(n) - call stack + set
    """

    def __init__(self):
        self.wanted = set()

    def findTarget(self, node: TreeNode, target: int) -> bool:
        if node is None:
            return False

        if node.val in self.wanted:
            return True

        self.wanted.add(target - node.val)
        return self.findTarget(node.left, target) or self.findTarget(node.right, target)
