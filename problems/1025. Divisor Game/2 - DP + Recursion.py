class Solution:
    def divisorGame(self, num: int, cache=None) -> bool:
        if num == 1:
            return False

        if cache is None:
            cache = {}

        if num in cache:
            return cache[num]

        for i in range(1, num // 2 + 1):
            if not num % i and not self.divisorGame(num - i, cache):
                cache[num] = True
                return True
        cache[num] = False
        return False
