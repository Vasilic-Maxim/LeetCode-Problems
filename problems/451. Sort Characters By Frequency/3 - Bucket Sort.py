from collections import Counter


class Solution:
    """
    Even though the time complexity is better that
    in first approach, hence we use a lot of memory
    for list structure the speed of the algorithm
    is worse.

    Time: O(n)
    Space: O(n)
    """

    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        order = [[] for _ in range(len(s))]
        result = []

        for key, count in counter.items():
            order[count - 1].append(key)

        for spot, items in enumerate(order):
            for char in items:
                result.extend([char] * (spot + 1))

        return "".join(reversed(result))
