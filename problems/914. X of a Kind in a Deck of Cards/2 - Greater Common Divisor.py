from functools import reduce
from math import gcd
from collections import Counter
from typing import List


class Solution:
    """
    To find GCD takes O(log (n)) time.

    Time: O(n * log (n))
    Space: O(n)
    """

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(gcd, Counter(deck).values()) != 1
