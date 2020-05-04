class Solution:
    def bitwiseComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i <<= 1

        return (i - 1 if num else i) ^ num
