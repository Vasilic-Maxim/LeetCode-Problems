class Solution:
    """
    Time: O(n)
    Space: O(n) - call stack with just ones (1)
    """

    def __init__(self):
        self.memo = {}

    def climbStairs(self, path: int) -> int:
        if path < 0:
            return 0

        if not path:
            return 1

        if path not in self.memo:
            self.memo[path] = (self.climbStairs(path - 1) +
                               self.climbStairs(path - 2))

        return self.memo[path]
