class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
