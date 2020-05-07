from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        wanted = {x, y}
        q = deque([root])
        while len(q):
            search_result = 0
            for _ in range(len(q)):
                node = q.popleft()

                # check if nodes in from queue contain wanted
                # values
                if node.val in wanted:
                    search_result += 1

                # if both x and y are children of the same node
                # then return False as a result
                if (node.left is not None and
                   node.right is not None and
                   {node.left.val, node.right.val} == wanted):
                    return False

                # add children to the queue
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            if search_result == 1:
                return False
            if search_result == 2:
                return True
