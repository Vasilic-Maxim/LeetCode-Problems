class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        """
        Time: O(2n) => O(n)
        Space: O(n)
        """

        def traverse(node: TreeNode, level: int) -> None:
            if node is None:
                return

            if len(levels_sums) == level:
                levels_sums.append(0)

            levels_sums[level] += node.val
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        levels_sums = [float("-inf")]
        traverse(root, 1)
        max_sum_level = 0
        for i in range(1, len(levels_sums)):
            if levels_sums[max_sum_level] < levels_sums[i]:
                max_sum_level = i

        return max_sum_level
