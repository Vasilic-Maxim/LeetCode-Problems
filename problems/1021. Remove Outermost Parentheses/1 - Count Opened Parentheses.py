class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def removeOuterParentheses(self, parentheses: str) -> str:
        result = []
        opened = 0
        for parenthesis in parentheses:
            is_right = parenthesis == "("
            opened += 1 if is_right else - 1
            if opened > (1 if is_right else 0):
                result.append(parenthesis)
        return "".join(result)
