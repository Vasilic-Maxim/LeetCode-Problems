class Solution:
    """
    Time: O(k * n) - 'insert' will take O(n) time each iteration
    Space: O(1)
    """

    def rotate(self, nums: list, k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop())
