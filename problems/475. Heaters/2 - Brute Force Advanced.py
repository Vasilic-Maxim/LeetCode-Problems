from typing import List


class Solution:
    """
    m - len(houses)
    n - len(heaters)
    Time: O(m * log (m) + n * log (n))
    Space: O(m + n)
    """

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        p, max_radius = 0, 0
        for house in houses:
            while p < len(heaters) - 1 and abs(heaters[p + 1] - house) <= abs(heaters[p] - house):
                p += 1
            max_radius = max(max_radius, abs(heaters[p] - house))
        return max_radius
