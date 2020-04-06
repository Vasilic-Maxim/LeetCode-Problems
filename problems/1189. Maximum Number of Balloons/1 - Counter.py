from collections import Counter


class Solution:
    """
    n - len("balloon")
    m - len(text)
    Time: O(n)
    Space: O(n + m)
    """
    def maxNumberOfBalloons(self, text: str) -> int:
        target_counter, text_counter = Counter("balloon"), Counter(text)
        result = float("inf")

        for key, val in target_counter.items():
            result = min(text_counter[key] // val, result)

        return result
