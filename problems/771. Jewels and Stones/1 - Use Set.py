class Solution:
    """
    n - length of 'stones'
    Time: O(n)
    Space: O(n)
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([True for i in stones if i in set(jewels)])
