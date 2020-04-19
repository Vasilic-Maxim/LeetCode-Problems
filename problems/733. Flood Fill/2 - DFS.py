from typing import List


class Solution:
    """
    n - len(image)
    m - len(image[0])

    Time: n * m
    Space: n * m
    """

    def floodFill(self, image: List[List[int]], x: int, y: int, new_color: int) -> List[List[int]]:
        if new_color != image[x][y]:
            self.dfs(image, x, y, new_color, image[x][y])

        return image

    def dfs(self, image: List[List[int]], x: int, y: int, new_color: int, old_color: int) -> None:
        if not (0 <= x < len(image)) or not (0 <= y < len(image[0])) or image[x][y] != old_color:
            return

        image[x][y] = new_color

        self.dfs(image, x - 1, y, new_color, old_color)
        self.dfs(image, x + 1, y, new_color, old_color)
        self.dfs(image, x, y - 1, new_color, old_color)
        self.dfs(image, x, y + 1, new_color, old_color)
