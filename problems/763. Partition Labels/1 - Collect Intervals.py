from collections import defaultdict
from typing import List


class Solution:
    """
    Time/Space: O(n)
    """

    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []

        chars = defaultdict(list)
        for i, char in enumerate(s):
            if char not in chars:
                chars[char] = [i, i]
            else:
                chars[char][1] = i

        intervals = list(chars.values())

        result = []
        current = intervals[0]
        for interval in intervals[1:]:
            if current[0] < interval[0] < current[1]:
                if interval[1] > current[1]:
                    current[1] = interval[1]
            else:
                result.append(current[1] - current[0] + 1)
                current = interval

        result.append(current[1] - current[0] + 1)

        return result
