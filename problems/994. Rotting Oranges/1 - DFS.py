from collections import deque
from typing import List


class Solution:
    """
    Time: O(m * n) each cell is visited at least once
    Space: O(m * n) in the worst case if all the oranges are rotten they will be added to the queue
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1

        cols = len(grid[0])
        fresh_count = 0
        rotten = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        minutes_passed = 0
        while rotten and fresh_count > 0:
            # update the number of minutes passed
            minutes_passed += 1

            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                # visit all the adjacent cells
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy

                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue

                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    fresh_count -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))

        # return the number of minutes taken to make all the fresh oranges to be rotten
        return minutes_passed if fresh_count == 0 else -1
