class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def reverseStr(self, s: str, k: int) -> str:
        char_list = list(s)

        for i in range(0, len(char_list), k * 2):
            char_list[i:i + k] = char_list[i:i + k][::-1]

        return "".join(char_list)
