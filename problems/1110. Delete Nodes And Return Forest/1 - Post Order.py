from typing import List, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        """
        Workflow:
        - recursively iterate throughout the tree and reassign
        the child-nodes if needed
        - if node is in the list of nodes that have to be deleted,
        then replace link of its parent with None value and add
        the node's children to the forest

        Complexity:
        Time: O(n)
        Space: O(f)

        Where:
        n = number of nodes in initial tree
        f = number of trees in the forest
        """

        def traverse(node: TreeNode) -> Union[TreeNode, None]:
            if node is None:
                return node

            node.left = traverse(node.left)
            node.right = traverse(node.right)

            if node.val not in targets:
                return node

            if node.left is not None:
                forest.append(node.left)
            if node.right is not None:
                forest.append(node.right)

            return None

        targets = set(to_delete)
        forest = []
        root = traverse(root)

        if root is not None:
            forest.append(root)

        return forest
