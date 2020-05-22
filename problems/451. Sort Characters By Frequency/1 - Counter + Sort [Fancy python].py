from collections import Counter


class Solution:
    """
    Counter(s).most_common() - sorts all keys by
    their values from bigger to lower.

    Time: O(n * log (n))
    Space: O(n)
    """

    def frequencySort(self, s: str) -> str:
        return "".join([key * count for key, count in Counter(s).most_common()])
