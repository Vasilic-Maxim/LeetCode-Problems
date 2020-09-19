from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        zero = ord("0")
        carry = 0
        result = []
        for n1, n2 in zip_longest(reversed(num1), reversed(num2)):
            n1 = 0 if n1 is None else ord(n1) - zero
            n2 = 0 if n2 is None else ord(n2) - zero
            carry, mod = divmod(n1 + n2 + carry, 10)
            result.append(str(mod))
        return "".join(result).reverse()
