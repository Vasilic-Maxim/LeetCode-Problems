class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def fizzBuzz(self, n: int) -> list:
        result = [str(i) for i in range(1, n + 1)]

        result[2:n:3] = ["Fizz"] * (n // 3)
        result[4:n:5] = ["Buzz"] * (n // 5)
        result[14:n:15] = ["FizzBuzz"] * (n // 15)

        return result
