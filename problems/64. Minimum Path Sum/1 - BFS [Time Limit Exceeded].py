from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        paths_sums = {}
        self.bfs(grid, paths_sums)
        return paths_sums[f'{len(grid)}-{len(grid[0])}']

    def bfs(self, grid: List[List[int]], paths_sums: dict, x: int = 0, y: int = 0, path_sum: int = 0) -> None:
        # out of grid, barrier for empty grid
        if x == len(grid) or y == len(grid[0]):
            return

        path_sum += grid[x][y]
        key = f"{x}-{y}"

        # the other iteration gave better results
        if paths_sums.get(key, float('inf')) <= path_sum:
            return

        paths_sums[key] = path_sum

        # call neighbors
        self.bfs(grid, paths_sums, x + 1, y, path_sum)
        self.bfs(grid, paths_sums, x, y + 1, path_sum)
