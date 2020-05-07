class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        counter = 0
        while x or y:
            if x % 2 != y % 2:
                counter += 1
            x >>= 1
            y >>= 1
        return counter
