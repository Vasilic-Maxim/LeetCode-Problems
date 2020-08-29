from typing import List


class Solution:
    """
    Time: O(n ** 2)
    Space: O(n)
    """

    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for i in range(len(arr) - 1, -1, -1):
            expected_value = i + 1
            if arr[i] != expected_value:
                index = arr.index(expected_value)
                if index != 0:
                    self.flip(arr, index + 1)
                    flips.append(index + 1)
                self.flip(arr, expected_value)
                flips.append(expected_value)

        return flips

    def flip(self, arr: List[int], i: int) -> None:
        arr[0:i] = reversed(arr[0:i])
