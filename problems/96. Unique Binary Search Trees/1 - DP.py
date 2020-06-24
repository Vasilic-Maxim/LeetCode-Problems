from functools import reduce
from typing import List


class Solution:
    """
    Lesson:
    https://www.youtube.com/watch?v=YDf982Lb84o

    Time: O(n)
    Space: O(n)
    """

    def numTrees(self, num: int) -> int:
        dp: List[int] = [1, 1]
        for i in range(2, num + 1):
            """
            1 - take a node from the the sequence
            2 - count all nodes from the left side (dp[y]) and
            from the right side (dp[i - y - 1]). We intentionally
            skip one node because one one the nodes must be the
            root of the tree
            3 - take already computed number of possible binary
            search trees for left and right sides and multiply them
            """
            dp.append(reduce(lambda x, y: x + dp[y] * dp[i - y - 1], range(i), 0))
        return dp[num]
