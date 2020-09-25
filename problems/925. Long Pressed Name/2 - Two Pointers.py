class Solution:
    """
    n = len(typed)
    Time: O(n)
    Space: O(1)
    """

    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, m = len(name), len(typed)
        i = j = 0
        while i < n and j < m:
            if name[i] != typed[j]:
                return False

            char = name[i]
            diff = j - i
            while i < n and char == name[i]:
                i += 1

            while j < m and char == typed[j]:
                j += 1

            if j - i - diff < 0:
                return False

        return i == n and j == m
