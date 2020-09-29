class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: TreeNode):
        """
        To solve the problem you may not restore the original values.
        All you have to do is to calculate the values for the nodes
        and add them to a set.

        Time/Space: O(2n) => O(n)
        """

        self.__values = set()
        root.val = 0
        self.__restore(root.left, 0, True)
        self.__restore(root.right, 0, False)
        self.__root = root

    def find(self, target: int) -> bool:
        """
        You also can calculate the path from target node to the
        root by using the same formula as for PQ implemented
        via arrays/list. Parent node id = (target - 1) // 2.

        Time/Space: O(1)
        """

        return target in self.__values

    def __restore(self, node: TreeNode, parent: int, is_left: bool) -> None:
        if node is None:
            return

        node.val = parent * 2 + (1 if is_left else 2)
        self.__values.add(node.val)
        self.__restore(node.left, node.val, True)
        self.__restore(node.right, node.val, False)
