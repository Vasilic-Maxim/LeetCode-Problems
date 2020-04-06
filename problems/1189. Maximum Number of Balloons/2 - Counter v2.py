from collections import Counter


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counter = Counter(text)
        return min(text_counter['b'],
                   text_counter['a'],
                   text_counter['l'] // 2,
                   text_counter['o'] // 2,
                   text_counter['n'])
