class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time/Space: O(n)
    """

    def deepestLeavesSum(self, root: TreeNode) -> int:
        max_depth = 0
        leaves_sum = 0

        def dfs(node: TreeNode, depth: int):
            if node is None:
                return

            nonlocal max_depth, leaves_sum
            if depth > max_depth:
                max_depth = depth
                leaves_sum = 0

            if depth == max_depth:
                leaves_sum += node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return leaves_sum
