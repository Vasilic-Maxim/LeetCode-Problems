class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def minAddToMakeValid(self, s: str) -> int:
        counter = opened = closed = 0
        for bracket in s:
            if bracket == "(":
                if closed != 0:
                    counter += closed
                    closed = 0
                opened += 1
            else:
                if opened:
                    opened -= 1
                else:
                    counter += 1

        return counter + opened
