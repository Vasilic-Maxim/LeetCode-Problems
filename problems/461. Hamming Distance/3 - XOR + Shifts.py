class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        counter = 0
        xor = x ^ y
        while xor:
            if xor % 2:
                counter += 1
            xor >>= 1
        return counter
