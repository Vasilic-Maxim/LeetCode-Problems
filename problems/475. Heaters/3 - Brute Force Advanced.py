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
        radius = i = 0
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
            if i == 0:
                radius = max(radius, heaters[i] - house)
            elif i == len(heaters):
                return max(radius, houses[-1] - heaters[-1])
            else:
                radius = max(radius, min(heaters[i] - house, house - heaters[i - 1]))
        return radius
