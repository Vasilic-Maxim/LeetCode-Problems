from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        """ Time/Space: O(n) """

        self.nodes = deque([root])

        for node in self.nodes:
            if node.left:
                self.nodes.append(node.left)
            if node.right:
                self.nodes.append(node.right)

    def insert(self, v: int) -> int:
        """ Time/Space: O(1) """

        n = len(self.nodes)
        self.nodes.append(TreeNode(v))
        parent = self.nodes[(n - 1) // 2]
        setattr(parent, ["right", "left"][n % 2], self.nodes[-1])

        return parent.val

    def get_root(self) -> TreeNode:
        return self.nodes[0]
