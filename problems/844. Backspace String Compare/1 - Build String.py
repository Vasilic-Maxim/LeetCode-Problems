class Solution:
    """
    n - len(first)
    m - len(second)
    Time: O(n + m)
    Space: O(n + m)
    """
    def backspaceCompare(self, first: str, second: str) -> bool:
        return self.translate(first) == self.translate(second)

    def translate(self, cipher: str) -> str:
        translation = []
        for char in cipher:
            if char != "#":
                translation.append(char)
            elif translation:
                translation.pop()
        return "".join(translation)
