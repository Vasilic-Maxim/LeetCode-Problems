from typing import List


class Solution:
    """
    m - len(commands)
    n - len(obstacles)
    Time: O(m + n)
    Space: O(n)
    """

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = result = 0

        for cmd in commands:
            if cmd == -2:  # left
                di = (di - 1) % 4
            elif cmd == -1:  # right
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
                        result = max(result, x * x + y * y)
        return result
