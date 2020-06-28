class Solution:
    """
    Time: O(n * sqrt(n))
    Space: O(n)
    """

    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        level = 0
        current_level = {0}

        while True:
            next_level = set()
            for path_sum in current_level:
                for square in squares:
                    if path_sum + square == n:
                        return level + 1
                    if path_sum + square < n:
                        next_level.add(path_sum + square)
            current_level = next_level
            level += 1
