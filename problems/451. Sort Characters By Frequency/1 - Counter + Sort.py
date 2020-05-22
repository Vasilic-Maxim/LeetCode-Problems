from collections import Counter


class Solution:
    """
    Time: O(n * log (n))
    Space: O(n)
    """

    def frequencySort(self, s: str) -> str:
        counter = Counter(s).most_common()
        order = sorted(counter.keys(), key=counter.get, reverse=True)
        return "".join([key * counter[key] for key in order])
