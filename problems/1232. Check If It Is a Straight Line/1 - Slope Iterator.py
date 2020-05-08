from typing import List


def slope_iterator(coordinates: List[List[int]]):
    fx, fy = coordinates[0]
    for sx, sy in coordinates[1:]:
        weight = sx - fx
        height = sy - fy
        yield weight / height if height else 0


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) > 2:
            slopes = slope_iterator(coordinates)
            slope = next(slopes)
            return all(slope == x for x in slopes)

        return True
