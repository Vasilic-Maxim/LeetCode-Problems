class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time/Space: O(n)
    """

    def findSecondMinimumValue(self, root: TreeNode):
        first = root.val
        second_so_far = float('inf')

        def dfs(node: TreeNode):
            nonlocal first, second_so_far
            if node:
                if first < node.val < second_so_far:
                    second_so_far = node.val
                elif node.val == first:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return second_so_far if second_so_far < float('inf') else -1
