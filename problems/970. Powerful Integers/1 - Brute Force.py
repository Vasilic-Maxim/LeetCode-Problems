from typing import List


class Solution:
    """
    Time: O(log bound)
    Space: O(log bound)
    """

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        for i in range(20):
            for j in range(20):
                power = x ** i + y ** j
                if power > bound:
                    break

                result.add(power)

                if y == 1:
                    break
            if x == 1:
                break

        return result
