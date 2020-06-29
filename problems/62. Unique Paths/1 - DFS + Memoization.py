class Solution:
    """
    Time: O(m * n)
    Space: O(m * n)
    """

    def uniquePaths(self, m: int, n: int, cache=None) -> int:
        if m < 0 or n < 0:
            return 0

        if cache is None:
            cache = {}

        if m == n == 1:
            return 1

        coord = (m, n)
        if coord not in cache:
            cache[coord] = self.uniquePaths(m - 1, n, cache) + self.uniquePaths(m, n - 1, cache)

        return cache[coord]
