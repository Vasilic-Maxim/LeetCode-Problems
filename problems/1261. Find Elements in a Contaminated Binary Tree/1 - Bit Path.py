class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: TreeNode):
        """
        To solve the problem you may not restore the original values.

        Time/Space: O(n)
        """

        root.val = 0
        self.__restore(root.left, 0, True)
        self.__restore(root.right, 0, False)
        self.root = root

    def find(self, target: int) -> bool:
        """
        You also can calculate the path from target node to the
        root by using the same formula as for PQ implemented
        via arrays/list. Parent node id = (target - 1) // 2.

        Time: O(log (n))
        Space: O(1)
        """

        node = self.root
        for bit in bin(target + 1)[3:]:
            node = node and (node.left, node.right)[int(bit)]
        return bool(node)

    def __restore(self, node: TreeNode, parent: int, is_left: bool) -> None:
        if node is None:
            return

        node.val = parent * 2 + (1 if is_left else 2)
        self.__restore(node.left, node.val, True)
        self.__restore(node.right, node.val, False)
