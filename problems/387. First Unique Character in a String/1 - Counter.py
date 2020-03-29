from collections import Counter


class Solution:
    """
    n - len(s)
    Time: O(n)
    Space: O(n) - space for 'counter' dict
    """

    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for idx, val in enumerate(s):
            if counter[val] == 1:
                return idx

        return -1
