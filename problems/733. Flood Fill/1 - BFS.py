from collections import deque
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
            initial_color = image[x][y]
            q = deque()
            q.append((x, y))
            while len(q):
                x, y = q.popleft()
                if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == initial_color:
                    image[x][y] = new_color

                    q.append((x - 1, y))
                    q.append((x + 1, y))
                    q.append((x, y - 1))
                    q.append((x, y + 1))

        return image
