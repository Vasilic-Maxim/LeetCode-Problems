class Solution:
    """
    n - len(s1)
    m - len(s2)
    Time: O(n + m)
    Space: O(1)
    """

    def checkInclusion(self, s1, s2):
        d1, d2 = {}, {}

        for char in s1:
            d1[char] = d1.get(char, 0) + 1

        for start, char in enumerate(s2):
            if start >= len(s1):
                d2[s2[start - len(s1)]] -= 1
                if not d2[s2[start - len(s1)]]:
                    del d2[s2[start - len(s1)]]

            d2[char] = d2.get(char, 0) + 1

            if d1 == d2:
                return True
        return False
