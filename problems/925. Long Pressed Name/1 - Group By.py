from itertools import groupby


class Solution(object):
    """
    Time: O(m + n)
    Space: O (m + n)
    """

    def isLongPressedName(self, name, typed):
        g1 = [(k, len(list(grp))) for k, grp in groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in groupby(typed)]

        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2
                   for (k1, v1), (k2, v2) in zip(g1, g2))
