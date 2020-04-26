from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def __init__(self):
        self.order_of_sums = defaultdict(int)
        self.counter = 0

    def pathSum(self, node: TreeNode, target_sum: int, last_sum: int = 0) -> int:
        if node is not None:
            curr_sum = last_sum + node.val

            if curr_sum == target_sum:
                self.counter += 1

            self.counter += self.order_of_sums[curr_sum - target_sum]
            self.order_of_sums[curr_sum] += 1
            self.pathSum(node.left, target_sum, curr_sum)
            self.pathSum(node.right, target_sum, curr_sum)
            self.order_of_sums[curr_sum] -= 1

        return self.counter
