class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def fizzBuzz(self, n: int) -> list:
        result = []
        for num in range(1, n + 1):
            key = f"{'Fizz' if not num % 3 else ''}{'Buzz' if not num % 5 else ''}"
            result.append(key or f"{num}")
        return result
