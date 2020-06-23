from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    That is one of the most obvious brute force solutions.
    Take in consideration that to count all the nodes we
    have to traverse all of them first. The last level of
    the complete tree, in case if it is also perfect tree,
    will take O(n / 2) space that is definitely less
    efficient than even DFS algorithm.

    Time: O(n)
    Space: O(n)
    """

    def countNodes(self, root: TreeNode) -> int:
        q = root is not None and deque([root])
        counter = 0
        while q:
            node = q.popleft()

            if node is None:
                break

            counter += 1
            q.append(node.left)
            q.append(node.right)
        return counter
