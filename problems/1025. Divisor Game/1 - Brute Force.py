class Solution:
    """
    Time: O(2 ** n)
    Space: O(log (n))
    """

    def divisorGame(self, num: int) -> bool:
        if num == 1:
            return False

        for i in range(1, num):
            if not num % i and self.divisorGame(num - i):
                return True
        return False
