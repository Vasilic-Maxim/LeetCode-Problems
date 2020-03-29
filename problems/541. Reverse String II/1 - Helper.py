class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def reverseStr(self, s: str, k: int) -> str:
        char_list = list(s)

        for i in range(0, len(char_list), k * 2):
            self.reverse(char_list, i, min(i + k - 1, len(char_list) - 1))

        return "".join(char_list)

    @staticmethod
    def reverse(chars: list, start: int, end: int):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
