class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        """
        Workflow:
        - traverse the tree using post-order and update the maximum
        depth of the leaves
        - if there is a node (might be a leaf) with which children's
        depths are equal to the maximum depth, then we find a candidate

        Complexity:
        Time: O(n)
        Space: O(1)

        Where:
        n = number of nodes
        """

        def traverse(node: TreeNode, depth: int) -> int:
            if node is None:
                return depth

            depth += 1

            nonlocal result, max_depth
            max_depth = max(max_depth, depth)

            left = traverse(node.left, depth)
            right = traverse(node.right, depth)

            if left == right == max_depth:
                result = node

            return max(left, right)

        max_depth = 0
        result = None
        traverse(root, 0)
        return result
