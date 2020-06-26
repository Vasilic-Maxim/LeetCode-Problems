class Solution:
    """
    For each tower, its surface area is 4 * v + 2
    However, 2 adjacent tower will hide the area of connected part.
    The hidden part is min(v1, v2) and we need just minus this area * 2

    Time: O(n ** 2)
    Space: O(1)
    """

    def surfaceArea(self, grid):
        n, res = len(grid), 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    res += 2 + grid[i][j] * 4

                if i:
                    res -= min(grid[i][j], grid[i - 1][j]) * 2

                if j:
                    res -= min(grid[i][j], grid[i][j - 1]) * 2
        return res
