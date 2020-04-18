class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    TIme: O(n)
    Space: O(n)
    """

    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = new_tail = None
        stack, node = [root], root
        while stack:
            if node.left is not None:
                node.left, node = None, node.left
                stack.append(node)
            else:
                node = stack.pop()

                if new_root is not None:
                    new_tail.right = node
                    new_tail = new_tail.right
                else:
                    new_root = new_tail = node

                if node.right is not None:
                    stack.append(node.right)
        return new_root
