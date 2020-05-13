class Solution:
    """
    Time: O(log (n))
    Space: O(1)
    """

    def binaryGap(self, num: int) -> int:
        last = None
        position = max_distance = 0
        while num:
            if num & 1:
                if last is not None:
                    max_distance = max(max_distance, position - last)
                last = position
            num >>= 1
            position += 1
        return max_distance
