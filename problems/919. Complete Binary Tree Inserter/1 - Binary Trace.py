class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        """
        Time: O(n)
        Space: O(log (n))
        """
        def nodes(node):
            if node is not None:
                yield 1
                yield from nodes(node.left)
                yield from nodes(node.right)

        self.root = root
        self.n = sum(nodes(root))

    def insert(self, v: int) -> int:
        """
        Time: O(log (n))
        Space: O(1)
        """

        directions = {"0": "left", "1": "right"}
        path = bin(self.n + 1)[3:]
        parent = self.root

        for step in path:
            direction = directions[step]
            child = getattr(parent, direction)
            if child is None:
                setattr(parent, direction, TreeNode(v))
            else:
                parent = parent[direction]

        self.n += 1
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root
