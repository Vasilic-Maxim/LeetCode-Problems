from math import sqrt
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(sqrt(area))

        while area % width != 0:
            width -= 1

        return [area // width, width]
