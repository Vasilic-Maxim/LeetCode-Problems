class Solution:
    """
    Time: O(log n)
    Space: O(1)
    """

    def isPerfectSquare(self, num: int) -> bool:
        root = 0
        bit = 1 << 15

        while bit > 0:
            root |= bit
            if root > num // root:
                root ^= bit
            bit >>= 1
        return root * root == num
